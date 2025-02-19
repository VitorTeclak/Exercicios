import os
import pymysql
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class veiculo:
    def __init__(self, modelo, ano, quilometragem, placa, valor, tipo):
        self.modelo = modelo
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

                    sql_veiculo = "INSERT INTO veiculo (tipo, modelo_veiculo, ano_producao, quilometragem, placa, valor) VALUES (%s, %s, %s, %s, %s, %s)"
                    valores_veiculo = (tipo, modelo_veiculo, ano, quilometragem, placa, valor_str)
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

                print("ID | Modelo | Ano | Quilometragem | Placa | Valor | Tipo")
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

                print("ID | Nome | CPF | Idade | Telefone | Email | ID Endereço")
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
                 
    