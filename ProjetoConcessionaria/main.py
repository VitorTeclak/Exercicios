import os

from entities.cliente import Cliente
from entities.veiculo import veiculo

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
    print('8. Excluir cliente')
    
    try:
        escolha = int(input('Digite a opção desejada: '))
    
        if escolha ==1:
            veiculo.inserir_veiculo()
        elif escolha ==2:
            veiculo.visualizar_veiculos()
        elif escolha ==3:
            veiculo.remover_veiculo()
        elif escolha ==4:
            veiculo.vender_veiculo()
        elif escolha ==5:
            veiculo.editar_dados_veiculo()
        elif escolha ==6:
            Cliente.inserir_cliente()
        elif escolha ==7:
            Cliente.visualizar_clientes()
        elif escolha ==8:
            Cliente.excluir_cliente()
        else:
            print("Opção invalida. Tente novamente")

        input('digite Enter para continuar ...')
    except ValueError:
        input("Valor invalido. Tente novamente.")
