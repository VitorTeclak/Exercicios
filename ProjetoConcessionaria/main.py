import os

from backend.entities.cliente import Cliente
from backend.entities.veiculo import veiculo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

print('Seja bem vindo ao sistema da concessionariaa')

while True:

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
                veiculo.vender_veiculo()
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
