import os

from entities.cliente import Cliente
from entities.veiculo import veiculo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

print('Seja bem vindo ao sistema da concessionariaa')

while True:

    clear()
    print('1. Adicionar Veiculo')
    print('2. Visualizar Veiculos')
    print('3. Remover Veiculo')
    print('4. Vender Veiculo')
    print('5. adicionar cliente')
    print('6. Visulizar clientes')
    print('7. Excluir cliente')
    
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
            Cliente.inserir_cliente()
        elif escolha ==6:
            Cliente.visualizar_clientes()
        elif escolha ==7:
            Cliente.excluir_cliente()
        else:
            print("Opção invalida. Tente novamente")

        input('digite Enter para continuar ...')
    except ValueError:
        input("Valor invalido. Tente novamente.")
