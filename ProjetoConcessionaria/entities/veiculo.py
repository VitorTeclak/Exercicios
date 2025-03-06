import os
import pymysql
from entities.cliente import Cliente
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class veiculo:
    def __init__(self, modelo, cor, ano, quilometragem, placa, valor, tipo):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.quilometragem = quilometragem
        self.placa = placa
        self.valor = valor
        self.tipo = tipo

    @staticmethod
    def inserir_veiculo():
        clear()
        try:   
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="senha",
                database="concessionaria",
            )

            with connection.cursor() as cursor:
                while True:
                    try:
                        tipo = input("Digite o tipo do veiculo (CARRO/MOTO): ").upper()
                        if tipo not in ["CARRO", "MOTO"]:
                            print("Tipo de veiculo invalido.")
                            continue  
                       
                        modelo_veiculo = input("Digite o modelo do veiculo: ").upper()
                        cor = input("Digite a cor do veiculo: ").upper()
                        ano = int(input("Digite o ano de fabricação do veiculo: "))
                        quilometragem =input("Digite a quilometragem do veiculo: ")
                        placa = input("Digite a placa do veiculo (Ex:AAA1111): ").upper()
                        
                        while True:
                            valor_flt = float(input("Digite o valor do veiculo: "))
                            if valor_flt == 0:
                                print("O valor do veiculo não pode ser 0. Tente novamente")
                            else: 
                                break
                        valor_str = f"{valor_flt:.3f}"
                            
                    except ValueError:
                        print("Dados do veiculo inválidos. Tente novamente.")

                    sql_veiculo = "INSERT INTO veiculo (tipo, modelo_veiculo, cor, ano_producao, quilometragem, placa, valor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    valores_veiculo = (tipo, modelo_veiculo, cor,  ano, quilometragem, placa, valor_str)
                    cursor.execute(sql_veiculo, valores_veiculo)

                    connection.commit()
                    print("Dados inseridos com sucesso!")
                    break


        except Exception as e:
            connection.rollback()
            print("Erro ao inserir dados:", e)

        finally:
            connection.close()  

    @staticmethod
    def visualizar_veiculos():
        clear()
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="senha",
        database="concessionaria"
)

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM veiculo")
                
                resultados = cursor.fetchall()

                print("ID | Modelo | Ano | Quilometragem | Placa | Valor | Tipo | ID_CLIENTE_COMPRADOR")
                print("-" * 70)
                for linha in resultados:
                    print(linha) 

        except Exception as e:
            print("Erro ao buscar os dados:", e)

        finally:
            connection.close() 

    @staticmethod
    def remover_veiculo():
        clear()
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="senha",
        database="concessionaria"
)

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM veiculo")
                
                resultados = cursor.fetchall()

                print("ID | MODELO | ANO | QUIOMETRAGEM | PLACA | VALOR | TIPO")
                print("-" * 70)
                for linha in resultados:
                    print(linha)
                id = int(input("Digite o numero ID do veiculo que deseja remover: "))

                try:
                    escolha = input(f"Tem certeza que deseja excluir o veiculo, ID: {id} (S/N)").upper()
                    if escolha == ("S"):


                        sql_del = "DELETE FROM veiculo WHERE id_veiculo = %s"
                        valores_del = (id)
                        cursor.execute(sql_del, valores_del)
                        connection.commit()
                        print("veiculo removido com sucesso.")
                        input("Digite ENTER para continuar.")
                    elif escolha == ("N"):
                        print("Operação cancelada")
                        input(" digite ENTER para continuar")
                except ValueError:
                    ...
        except Exception as e:
            print("Erro ao buscar os dados:", e)

        finally:
            connection.close()  
    
    @staticmethod
    def vender_veiculo():
        clear()
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="senha",
        database="concessionaria")
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_veiculo, modelo_veiculo, placa, tipo FROM veiculo")
                resultados_veiculos = cursor.fetchall()

                print("ID | MODELO | PLACA | TIPO")
                print("-" * 70)
                for linha in resultados_veiculos:
                    print(linha)
                try:
                    id_veiculo = int(input("Digite o numero ID do veiculo que deseja vender: "))
                except ValueError:
                    print("Id veiculo invalido.")
                    
                cursor.execute("SELECT id_cliente, nome, email FROM cliente")
                resultados_cliente = cursor.fetchall()
                print("ID CLIENTE | NOME| EMAIL")
                print("-" * 70)
                for linha in resultados_cliente:
                    print(linha)
                try: 
                    id_cliente = int(input("Digite o id no cliente que ira comprar o carro: "))
                except ValueError:
                    print("Id invalido.")

                try:
                    escolha = input(f"Tem certeza que deseja vender o veiculo, ID: {id_veiculo} para o cliente ID: {id_cliente} (S/N)").upper()
                    if escolha == ("S"):
                        sql_upt = "UPDATE veiculo SET id_cliente = %s WHERE id_veiculo = %s;"
                        valores_upt = (id_cliente, id_veiculo)
                        cursor.execute(sql_upt, valores_upt)
                        connection.commit()
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
        
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="senha",
        database="concessionaria")
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_veiculo, modelo_veiculo, cor, ano_producao, placa, valor, tipo FROM veiculo")
                resultados_cliente = cursor.fetchall()
                print("ID_VEICULO | MODELO_VEICULO | COR | ANO_PRODUCAO | PLACA | VALOR | TIPO")
                print("-" * 70)
                for linha in resultados_cliente:
                    print(linha)    
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
                    if coluna_a_editar == "ano_producao":
                        novo_valor_coluna = int(input("Digite a coluna que deseja editar: "))
                    else:
                        novo_valor_coluna = input("Digite o novo valor: ").upper()
                    
                except ValueError:
                    print("Valores invalidos tente novamente.")
        
                sql_upt = "UPDATE veiculo SET {} = %s WHERE id_veiculo = %s".format(coluna_a_editar)
                valores_upt = (novo_valor_coluna, id_veiculo)
                cursor.execute(sql_upt, valores_upt)
                connection.commit()
                print("Valores alterados com sucesso. ")

        except Exception as e:
            print("Erro ao buscar os dados:", e)
        finally:
            connection.close()  
    
    