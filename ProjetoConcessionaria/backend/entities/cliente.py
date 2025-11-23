import os
import pymysql
import polars as pl
from backend.config.database import Settings
from sqlalchemy import create_engine, text
from backend.auxiliar.formataQuery import formatarResultados
MYSQLALCHEMY_DATABASE_EXPERT_URL = Settings.DATABASEMYSQL_EXPERT_URL
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



class endereco:
    def __init__ (self, rua,numero, cep, bairro ):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.bairro = bairro
        
class Cliente:
    @staticmethod
    def inserir_cliente():
        clear()
        try:

            while True:
                try:
                    rua = input("Digite a rua do cliente: ")
                    numero = int(input("Digite o número da casa do cliente: "))
                    cep = input("Digite o CEP do cliente: ")
                    bairro = input("Digite o bairro do cliente: ")
                    complemento = input("Observação/complemento de endereço: ")
                except ValueError:
                    print("Valores de endereço inválidos. Tente novamente.")

                try:
                    nome = input("Digite o nome do cliente: ")
                    cpf = input("Digite o CPF do cliente: ")
                    idade = int(input("Digite a idade do cliente: "))
                    telefone = input("Digite o telefone do cliente: ")
                    email = input("Digite o email do cliente: ")
                    break
                except ValueError:
                    print("Dados do cliente inválidos. Tente novamente.")

            cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

            with cnn.connect() as conn:
                result = conn.execute(
                    text("""
                        INSERT INTO endereco (rua, numero, cep, bairro, complemento)
                        VALUES (:rua, :numero, :cep, :bairro, :complemento)
                    """),
                    {
                        "rua": rua,
                        "numero": numero,
                        "cep": cep,
                        "bairro": bairro,
                        "complemento": complemento
                    }
                )
                conn.commit()
                id_endereco = result.lastrowid

                result = conn.execute(
                    text("""
                            INSERT INTO pessoa 
                                (nome, cpf, idade, telefone, email, id_endereco)
                            VALUES
                                (:nome, :cpf, :idade, :telefone, :email, :id_endereco)"""),
                                {
                                    "nome" : nome,
                                    "cpf" : cpf,
                                    "idade" : idade,
                                    "telefone" : telefone,
                                    "email" : email,
                                    "id_endereco" : id_endereco
                                }
                )
                conn.commit()    
            print("Dados inseridos com sucesso!")
            return result

        except Exception as e:
            
            print("Erro ao inserir dados:", e)


    

    @staticmethod
    def visualizar_clientes():
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

        try:
            query = text("""SELECT 
                                p.id_pessoa, 
                                p.nome, 
                                p.cpf, 
                                p.idade, 
                                p.telefone, 
                                p.email, 
                                e.rua, 
                                e.numero, 
                                e.cep 
                            FROM pessoa p
                            INNER JOIN 
                                endereco e ON p.id_endereco = e.id_endereco;""")

            # Conectando e executando a query
            with cnn.connect() as connection:
                resultados = connection.execute(query)
                formatarResultados(resultados)
                
        except Exception as e:
            print("Erro ao buscar os dados:", e)

    
    @staticmethod
    def excluir_cliente():
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

        try:
            
            query = text("""
                            SELECT
                                id_pessoa,
                                nome,
                                cpf,
                                id_endereco
                            FROM
                                pessoa""")

            # Conectando e executando a query
            with cnn.begin() as conn:
                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                

                formatarResultados(resultados)
                id = int(input("Digite o numero ID do cliente que deseja remover: "))

                try:
                    escolha = input(f"Tem certeza que deseja excluir o cliente ID: {id} (S/N)").upper()
                    if escolha == ("S"):
                        
                            
                            
                        print(df)
                        df_filtrado = df.filter(pl.col("id_pessoa") == id)
                        id_endereco = df_filtrado.select("id_endereco")[0, 0]  

                        query = text(f"""
                            SELECT COUNT(*) AS total
                            FROM vendas
                            WHERE id_cliente = :id_cliente
                            """)

                        resultado = conn.execute(query, {"id_cliente": id})
                        total = resultado.scalar()  

                        if total != 0:
                            print("Existe venda registrada no cliente, por questões de regras da empresa o cliente não pode ser removido")
                            return
                        
                        result = conn.execute(
                            text("""
                                DELETE FROM 
                                    pessoa
                                WHERE 
                                    id_pessoa = :id
                            """),
                            {"id": id}
                            )
                        conn.commit() 

                        result = conn.execute(
                            text("""
                                DELETE FROM
                                    endereco
                                WHERE
                                    id_endereco = :id_endereco
                                """),
                                {"id_endereco": id_endereco}
                        )
                        conn.commit()

                                
                                


                        cnn.execute(query)
                        print("Cliente removido com sucesso.")
                        input("Digite ENTER para continuar.")
                    elif escolha == ("N"):
                        print("Operação cancelada")
                        input(" digite ENTER para continuar")
                except ValueError:
                    ...
        except Exception as e:
            print("Erro ao buscar os dados:", e)

    @staticmethod
    def editar_cliente():
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)
        try:
            
            query = text("SELECT id_pessoa as id_cliente, nome, cpf, idade, telefone, email FROM pessoa")
            with cnn.connect() as conn:
                resultados = conn.execute(query)
                formatarResultados(resultados)
                try:
                    id_cliente = int(input("Digite o ID do veiculo que deseja editar: "))
                except ValueError:
                    print("Id invalido.")
                try:
                    print("NOME | CPF | IDADE | TELEFONE | EMAIL")
                    print("OBS: Digite exatamente igual.")
                    coluna_a_editar = input("Digite a coluna que deseja editar: ").lower()
                    colunas_validas = ["id_cliente", "nome", "cpf", "idade", "telefone", "email"]
                    if coluna_a_editar not in colunas_validas:
                        print("Opção digitada não esta valida no banco de dados.")
                        return
                    novo_valor_coluna = input("Digite o novo valor: ").upper()
                    
                except ValueError:
                    print("Valores invalidos tente novamente.")
    
                query = text(f"""
                    UPDATE pessoa
                    SET {coluna_a_editar} = :novo_valor
                    WHERE id_pessoa = :id_pessoa
                """)

                with cnn.connect() as conn:
                    conn.execute(query, {"novo_valor": novo_valor_coluna, "id_pessoa": id_cliente})
                    conn.commit() 
                print("Valores Atualizados")
        except Exception as e:
            print("Erro ao buscar os dados:", e)

    


