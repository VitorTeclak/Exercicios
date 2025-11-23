import os
import pymysql
import polars as pl
from backend.entities.cliente import Cliente
from backend.config.database import Settings
from sqlalchemy import create_engine, text
from backend.auxiliar.formataQuery import formatarResultados
MYSQLALCHEMY_DATABASE_EXPERT_URL = Settings.DATABASEMYSQL_EXPERT_URL
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


    


    
                


class veiculo:
    @staticmethod
    def inserir_veiculo():
        clear()
        try:   
            
            while True:
                try:
                    tipo = input("Digite o tipo do veiculo (CARRO/MOTO): ").upper()
                    if tipo not in ["CARRO", "MOTO"]:
                        print("Tipo de veiculo invalido.")
                        continue  
                    print(tipo)
                    modelo_veiculo = input("Digite o modelo do veiculo: ").upper()
                    cor = input("Digite a cor do veiculo: ").upper()
                    ano = input("Digite o ano de fabricação do veiculo: ")
                    quilometragem =input("Digite a quilometragem do veiculo: ")
                    placa = input("Digite a placa do veiculo (Ex:AAA1111): ").upper()
                    while True:
                        valor_flt = float(input("Digite o valor do veiculo: "))
                        if valor_flt == 0:
                            print("O valor do veiculo não pode ser 0. Tente novamente")
                        else:
                            valor_str = f"{valor_flt:.2f}"
                            break
                    break
                        
                except ValueError:
                    print("Dados do veiculo inválidos. Tente novamente.")

            cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

            with cnn.begin() as conn:
                result = conn.execute(
                    text("""
                    INSERT INTO veiculo (tipo, modelo_veiculo, cor, ano_producao, quilometragem, placa, valor)
                    VALUES (:tipo, :modelo_veiculo, :cor, :ano_producao, :quilometragem, :placa, :valor)
                """),
                {   
                    "tipo" : tipo,
                    "modelo_veiculo": modelo_veiculo,
                    "cor": cor,
                    "ano_producao": ano,
                    "quilometragem": quilometragem,
                    "placa": placa,
                    "valor" : valor_str
                }
            )
                print("Veiculo inserido")
            conn.commit()

        except Exception as e:
            print("Erro ao inserir dados:", e)


    @staticmethod
    def visualizar_veiculos():
        clear()
        try:
            cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

            with cnn.begin() as conn:
                query = text("""
                            SELECT 
                                *
                            FROM
                                veiculo
                            """)
                
                with cnn.connect() as connection:
                    resultados = connection.execute(query)
                    formatarResultados(resultados)
                
        except Exception as e:
            print("Erro ao buscar os dados:", e)

        finally:
            connection.close() 

    @staticmethod
    def remover_veiculo():
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

        try:
            
            query = text("""
                            SELECT
                                *
                            FROM
                                veiculo""")

            # Conectando e executando a query
            with cnn.begin() as conn:
                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                

                formatarResultados(resultados)
                id = int(input("Digite o numero ID do veiculo que deseja excluir: "))

                try:
                    escolha = input(f"Tem certeza que deseja excluir o veiculo, ID: {id} (S/N)").upper()
                    if escolha == ("S"):

                        query = text(f"""
                            SELECT COUNT(*) AS total
                            FROM vendas
                            WHERE id_veiculo = :id_veiculo
                            """)

                        resultado = conn.execute(query, {"id_veiculo": id})
                        total = resultado.scalar()  

                        if total != 0:
                            print("Existe venda registrada no veiculo, por questões de regras da empresa o veiculo não pode ser removido")
                            return
                        result = conn.execute(
                            text("""
                                DELETE FROM 
                                    veiculo
                                WHERE 
                                    id_veiculo = :id
                            """),
                            {"id": id}
                            )
                        conn.commit() 
                        
                        print("veiculo removido com sucesso.")
                        input("Digite ENTER para continuar.")
                    elif escolha == ("N"):
                        print("Operação cancelada")
                        input(" digite ENTER para continuar")
                except ValueError:
                    ...
        except Exception as e:
            print("Erro ao buscar os dados:", e)


    
    @staticmethod
    def vender_veiculo(id_funcionario):
        clear()
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)
        try:
            
            query = text("""
                            SELECT id_veiculo, modelo_veiculo, placa, tipo FROM veiculo
                        """)

            # Conectando e executando a query
            with cnn.begin() as conn:
                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                formatarResultados(resultados)

                try:
                    id_veiculo = int(input("Digite o numero ID do veiculo que deseja vender: "))
                except ValueError:
                    print("Id veiculo invalido.")
                    
                query = text("""
                            SELECT 
                             *

                            FROM pessoa

                        """)

                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                formatarResultados(resultados)
                try: 
                    id_cliente = int(input("Digite o id no cliente que ira comprar o carro: "))
                except ValueError:
                    print("Id invalido.")

                try:
                    escolha = input(f"Tem certeza que deseja vender o veiculo, ID: {id_veiculo} para o cliente ID: {id_cliente} (S/N)").upper()
                    if escolha == ("S"):
                        result = conn.execute(
                            text("""
                                    INSERT INTO vendas 
                                        (id_funcionario, id_pessoa, id_veiculo)
                                    VALUES
                                        (:id_funcionario, :id_pessoa, :id_veiculo)"""),
                                        {
                                            "id_funcionario" : id_funcionario,
                                            "id_pessoa" : id_cliente,
                                            "id_veiculo" : id_veiculo
                                            
                                        }
                        )
                        conn.commit()    
                        print("veiculo vendido com sucesso.")
                        input("Digite ENTER para continuar.")
                    elif escolha == ("N"):
                        print("Operação cancelada")
                        input(" digite ENTER para continuar")
                except ValueError:
                    ...
                



        except Exception as e:
            print("Erro ao buscar os dados:", e)

    @staticmethod
    def editar_dados_veiculo():
        clear()
        
        cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)
        try:
            query = text(("SELECT id_veiculo, modelo_veiculo, cor, ano_producao, placa, valor, tipo FROM veiculo"))
            with cnn.begin() as conn:
                resultados = conn.execute(query)
                df = pl.read_database(query, cnn, infer_schema_length=10000)
                
                formatarResultados(resultados)
                try:
                    id_veiculo = int(input("Digite o ID do veiculo que deseja editar: "))
                except ValueError:
                    print("Id invalido.")
                try:
                    print("MODELO_VEICULO | COR | ANO_PRODUCAO | QUIOMETRAGEM | PLACA | VALOR | TIPO")
                    print("OBS: Digite exatamente igual.")
                    coluna_a_editar = input("Digite a coluna que deseja editar: ").lower()
                    colunas_validas = ["modelo_veiculo", "cor", "ano_producao", "quilometragem", "placa", "valor", "tipo"]
                    if coluna_a_editar not in colunas_validas:
                        print("Opção digitada não esta valida no banco de dados.")
                    novo_valor_coluna = input("Digite o novo valor: ").upper()
                    
                except ValueError:
                    print("Valores invalidos tente novamente.")
        
                query = text(f"""
                    UPDATE veiculo
                    SET {coluna_a_editar} = :novo_valor
                    WHERE id_veiculo = :id_veiculo
                """)

                with cnn.connect() as conn:
                    conn.execute(query, {"novo_valor": novo_valor_coluna, "id_veiculo": id_veiculo})
                    conn.commit() 
                print("Valores alterados com sucesso. ")

        except Exception as e:
            print("Erro ao buscar os dados:", e)

    
    