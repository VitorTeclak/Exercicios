import os
import pymysql
import polars as pl
import random
import bcrypt
from backend.config.database import Settings
from sqlalchemy import create_engine, text
from backend.auxiliar.formataQuery import formatarResultados
from backend.entities.cliente import Cliente
MYSQLALCHEMY_DATABASE_EXPERT_URL = Settings.DATABASEMYSQL_EXPERT_URL
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def cria_login():
    numero = "".join(random.choices("0123456789", k=7))
    login  = "A@" + numero
    return login


def coloca_nivel_de_acesso(cargo):
    if cargo == 'vendedor':
        return 1
    elif cargo == 'rh':
        return 2
    elif cargo == 'supervisor_de_vendas':
        return 3
    elif cargo == 'gerente':
        return 4


class Funcionario:
    @staticmethod
    def inserir_funcionario():
        clear()
        try:

            while True:
                try:
                    rua = input("Digite a rua do funcionário: ")
                    numero = int(input("Digite o número da casa do funcionário: "))
                    cep = input("Digite o CEP do funcionário: ")
                    bairro = input("Digite o bairro do funcionário: ")
                    complemento = input("Observação/complemento de endereço: ")
                except ValueError:
                    print("Valores de endereço inválidos. Tente novamente.")

                try:
                    nome = input("Digite o nome do funcionário: ")
                    cpf = input("Digite o CPF do funcionário: ")
                    idade = int(input("Digite a idade do funcionário: "))
                    telefone = input("Digite o telefone do funcionário: ")
                    email = input("Digite o email do funcionário: ")
                    cargo = input("Digite o cargo do funcionário (Vendedor | Supervisor_de_vendas |Gerente | RH')").lower()
                    if cargo not in ('vendedor','supervisor_de_vendas','gerente','rh'):
                        print("Cargo invalido")
                    nivel_acesso = coloca_nivel_de_acesso(cargo)
                    login = cria_login()
                    senha = input("peça para o funcionario escolher uma senha: ")
                    hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
                    break
                except ValueError:
                    print("Dados do funcionário inválidos. Tente novamente.")

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
                id_funcionario = result.lastrowid
                result = conn.execute(
                    text("""
                            INSERT INTO funcionario 
                                (id_pessoa, cargo, nivel_acesso, login, senha)
                            VALUES
                                (:id_pessoa, :cargo, :nivel_acesso, :login, :senha)"""),
                                {
                                    "id_pessoa" : id_funcionario,
                                    "cargo" : cargo,
                                    "nivel_acesso" : nivel_acesso,
                                    "login" : login,
                                    "senha" : hash_senha
                                    
                                }
                )
                conn.commit()
            print("Dados inseridos com sucesso!")
            return result

        except Exception as e:
            
            print("Erro ao inserir dados:", e)


    @staticmethod
    def visualizar_funcionarios():
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

        try:
            query = text("""
                        SELECT 
                            f.id_funcionario, 
                            f.cargo,
                            p.nome, 
                            p.cpf, 
                            p.idade, 
                            p.telefone, 
                            p.email, 
                            e.rua, 
                            e.numero, 
                            e.cep 
                        FROM 
                            funcionario f
                        INNER JOIN pessoa p 
                            ON p.id_pessoa = f.id_pessoa
                        INNER JOIN endereco e 
                            ON e.id_endereco = p.id_endereco;
                            """)

            # Conectando e executando a query
            with cnn.connect() as connection:
                resultados = connection.execute(query)
                formatarResultados(resultados)
                
        except Exception as e:
            print("Erro ao buscar os dados:", e)

    @staticmethod
    def editar_funcionario():
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)
        try:
            
            query = text("""
                        SELECT 
                            f.id_funcionario, 
                            p.nome,
                            p.cpf,
                            f.cargo
                        FROM funcionario f
                        INNER JOIN pessoa p 
                            ON p.id_pessoa = f.id_pessoa
                        """)
            with cnn.connect() as conn:
                resultados = conn.execute(query)
                formatarResultados(resultados)
                try:
                    id_cliente = int(input("Digite o ID do veiculo que deseja editar: "))
                except ValueError:
                    print("Id invalido.")
                try:
                    print("NOME | CPF | CARGO")
                    print("OBS: Digite exatamente igual.")
                    coluna_a_editar = input("Digite a coluna que deseja editar: ").lower()
                    colunas_validas = ["nome", "cpf", "cargo"]
                    if coluna_a_editar not in colunas_validas:
                        print("Opção digitada não esta valida no banco de dados.")
                        return
                    
                    novo_valor_coluna = input("Digite o novo valor: ").upper()
                    if coluna_a_editar == 'cargo':  
                        if coluna_a_editar not in ('vendedor','supervisor_de_vendas','gerente','rh'):
                            print("Opção digitada é.")
                            return
                    
                except ValueError:
                    print("Valores invalidos tente novamente.")
    
                query = text(f"""
                    UPDATE funcionario
                    SET {coluna_a_editar} = :novo_valor
                    WHERE id_pessoa = :id_pessoa
                """)

                with cnn.connect() as conn:
                    conn.execute(query, {"novo_valor": novo_valor_coluna, "id_pessoa": id_cliente})
                    conn.commit() 
                print("Valores Atualizados")
        except Exception as e:
            print("Erro ao buscar os dados:", e)



    @staticmethod
    def excluir_funcionario():
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

        try:
            
            query = text("""
                            SELECT 
                                f.id_funcionario, 
                                p.nome,
                                p.cpf,
                                f.cargo
                        FROM funcionario f
                        INNER JOIN pessoa p 
                            ON p.id_pessoa = f.id_pessoa
                        """)

            with cnn.begin() as conn:
                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                

                formatarResultados(resultados)
                id = int(input("Digite o numero ID do funcionario que deseja remover: "))

                try:
                    escolha = input(f"Tem certeza que deseja excluir o cliente ID: {id} (S/N)").upper()
                    if escolha == ("S"):
                        
                            
                            
                        print(df)
                        df_filtrado = df.filter(pl.col("id_pessoa") == id)
                        id_endereco = df_filtrado.select("id_endereco")[0, 0]  

                        query = text(f"""
                            SELECT COUNT(*) AS total
                            FROM vendas
                            WHERE id_funcionario = :id_funcionario
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

                        result = conn.execute(
                            text("""
                                DELETE FROM
                                    funcionario
                                WHERE
                                    id_funcionario = :id_funcionario
                                """),
                                {"id_funcionario": id}
                        )
                        conn.commit()

                                
                                


                        cnn.execute(query)
                        print("Funcionario removido com sucesso.")
                        input("Digite ENTER para continuar.")
                    elif escolha == ("N"):
                        print("Operação cancelada")
                        input(" digite ENTER para continuar")
                except ValueError:
                    ...
        except Exception as e:
            print("Erro ao buscar os dados:", e)



