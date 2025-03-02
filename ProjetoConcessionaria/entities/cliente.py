import os
import pymysql
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class endereco:
    def __init__ (self, rua,numero, cep, bairro ):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.bairro = bairro
        
class Cliente:
    def __init__(self, nome, cpf, idade, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @staticmethod
    def inserir_cliente():
        clear()
        try:
            
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="1421",
                database="concessionaria",
            )

            with connection.cursor() as cursor:
                while True:
                    try:
                        rua = input("Digite a rua do cliente: ")
                        numero = int(input("Digite o número da casa do cliente: "))
                        cep = input("Digite o CEP do cliente: ")
                        bairro = input("Digite o bairro do cliente: ")
                        complemento = input("Observação/complemento de endereço: ")
                        break
                    except ValueError:
                        print("Valores de endereço inválidos. Tente novamente.")

                while True:
                    try:
                        nome = input("Digite o nome do cliente: ")
                        cpf = input("Digite o CPF do cliente: ")
                        idade = int(input("Digite a idade do cliente: "))
                        telefone = input("Digite o telefone do cliente: ")
                        email = input("Digite o email do cliente: ")
                        break
                    except ValueError:
                        print("Dados do cliente inválidos. Tente novamente.")

                sql_endereco = "INSERT INTO endereco (rua, numero, cep, bairro, complemento) VALUES (%s, %s, %s, %s, %s)"
                valores_endereco = (rua, numero, cep, bairro, complemento)
                cursor.execute(sql_endereco, valores_endereco)

 
                id_endereco = cursor.lastrowid

                sql_cliente = "INSERT INTO cliente (nome, cpf, idade, telefone, email, id_endereco) VALUES (%s, %s, %s, %s, %s, %s)"
                valores_cliente = (nome, cpf, idade, telefone, email, id_endereco)
                cursor.execute(sql_cliente, valores_cliente)

                connection.commit()
                print("Dados inseridos com sucesso!")

        except Exception as e:
            connection.rollback()
            print("Erro ao inserir dados:", e)

        finally:
            connection.close()  
    
    @staticmethod
    def visualizar_clientes():
        clear()
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1421",
        database="concessionaria"
)

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cliente")
                
                resultados = cursor.fetchall()

                print("ID | Nome | CPF | Idade | Telefone | Email | ID Endereço")
                print("-" * 70)
                for linha in resultados:
                    print(linha) 

        except Exception as e:
            print("Erro ao buscar os dados:", e)

        finally:
            connection.close()  
    
    @staticmethod
    def excluir_cliente():
        clear()
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1421",
        database="concessionaria"
)

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cliente")
                
                resultados = cursor.fetchall()

                print("ID | Nome | CPF | Idade | Telefone | Email | ID Endereço")
                print("-" * 70)
                for linha in resultados:
                    print(linha)
                id = int(input("Digite o numero ID do cliente que deseja remover: "))

                try:
                    escolha = input(f"Tem certeza que deseja excluir o cliente ID: {id} (S/N)").upper()
                    if escolha == ("S"):


                        sql_del = "DELETE FROM cliente WHERE id_cliente = %s"
                        valores_del = (id)
                        cursor.execute(sql_del, valores_del)
                        connection.commit()
                        print("Cliente removido com sucesso.")
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
                


