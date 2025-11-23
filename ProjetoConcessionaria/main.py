import os
import requests

from backend.entities.cliente import Cliente
from backend.entities.veiculo import veiculo
from backend.entities.funcionario import Funcionario

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

API = "http://127.0.0.1:8000"

clear()
while True:
    
    login = input('digite o login')
    senha = input('digite a senha')
    r = requests.post(f"{API}/login", json={"login": login, "senha": senha})
    resp = r.json()
    
    if resp.get("status") == "Autenticado":
        nivel = resp.get("nivel")
        id = resp.get("id")
        print(f"Login OK! Nível de acesso: {nivel}")
        break
    else:
        print("Login invalido tente novamente")

print('Seja bem vindo ao sistema da concessionaria')

while True:

    if nivel == 1: #Vendedor
        clear()
        print('1. Visualizar Veiculos')
        print('2. Vender Veiculo')
        print('3. adicionar cliente')
        print('4. Visulizar clientes')
        print('5. Editar dados do Cliente')
        try:
            escolha = int(input('Digite a opção desejada: '))

            match escolha:
                case 1:
                    veiculo.visualizar_veiculos()
                case 2:
                    veiculo.vender_veiculo(id)
                case 3:
                    Cliente.inserir_cliente()
                case 4:
                    Cliente.visualizar_clientes()
                case 5:
                    Cliente.editar_cliente()
                case _:
                    print("Opção inválida. Tente novamente")
            input('Digite Enter para continuar ...')

        except ValueError:
            input("Valor inválido. Tente novamente.")

    elif nivel == 2: #Lider
        clear()
        print('1. Adionar Veiculo')
        print('2. Visualizar Veiculos')
        print('3. Remover Veiculo')
        print('4. Vender Veiculo')
        print('5. Editar dados do Veiculo')
        print('6. adicionar cliente')
        print('7. Visulizar clientes')
        print('8. Editar dados do Cliente')
        print('9. Excluir cliente')
        try:
            escolha = int(input('Digite a opção desejada: '))

            match escolha:
                case 1:
                    veiculo.inserir_veiculo()
                case 2:
                    veiculo.visualizar_veiculos()
                case 3:
                    veiculo.remover_veiculo()
                case 4:
                    veiculo.vender_veiculo(id)
                case 5:
                    veiculo.editar_dados_veiculo()
                case 6:
                    Cliente.inserir_cliente()
                case 7:
                    Cliente.visualizar_clientes()
                case 8:
                    Cliente.editar_cliente()
                case 9:
                    Cliente.excluir_cliente()
                case _:
                    print("Opção inválida. Tente novamente")
                    input('Digite Enter para continuar ...')

        except ValueError:
            input("Valor inválido. Tente novamente.")


    elif nivel == 3: #RH
        clear()
        print('1. Adionar Funcionario')
        print('2. Visualizar Funcionarios')
        print('3. Editar Funcionarios')
        print('4. Excluir Funcionario')
        
        try:
            escolha = int(input('Digite a opção desejada: '))

            match escolha:
                case 1:
                    Funcionario.inserir_funcionario()
                case 2:
                    Funcionario.visualizar_funcionarios()
                case 3:
                    Funcionario.editar_funcionario()
                case 4:
                    Funcionario.excluir_funcionario()
                case _:
                    print("Opção inválida. Tente novamente")
                    input('Digite Enter para continuar ...')

        except ValueError:
            input("Valor inválido. Tente novamente.")
    elif nivel == 4: #Gerente
        clear()
        print('1. Adionar Veiculo')
        print('2. Visualizar Veiculos')
        print('3. Remover Veiculo')
        print('4. Vender Veiculo')
        print('5. Editar dados do Veiculo')
        print('6. adicionar cliente')
        print('7. Visulizar clientes')
        print('8. Editar dados do Cliente')
        print('9. Excluir cliente')
        print('10. Adionar Funcionario')
        print('11. Visualizar Funcionarios')
        print('12. Editar Funcionarios')
        print('13. Excluir Funcionario')
    
    try:
        escolha = int(input('Digite a opção desejada: '))

        match escolha:
            case 1:
                ...
            case 2:
                veiculo.visualizar_veiculos()
            case 3:
                veiculo.remover_veiculo()
            case 4:
                veiculo.vender_veiculo(id)
            case 5:
                veiculo.editar_dados_veiculo()
            case 6:
                Cliente.inserir_cliente()
            case 7:
                Cliente.visualizar_clientes()
            case 8:
                Cliente.editar_cliente()
            case 9:
                Cliente.excluir_cliente()
            case 10:
                Funcionario.inserir_funcionario()
            case 11:
                Funcionario.visualizar_funcionarios()
            case 12:
                Funcionario.editar_funcionario()
            case 13:
                Funcionario.excluir_funcionario()
            case _:
                print("Opção inválida. Tente novamente")

        input('Digite Enter para continuar ...')

    except ValueError:
        input("Valor inválido. Tente novamente.")
