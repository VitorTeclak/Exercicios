import os

from entities.cliente import Cliente
from entities.veiculo import veiculo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

print('Seja bem vindo ao sistema da concessionÃ¡ria')

while True:

    clear()
    print('1. Adicionar Veiculo')
    print('2. Visualizar Veiculos')
    print('3. Remover Veiculo')
    print('4. adicionar cliente')
    print('5. Visulizar clientes')
    print('6. Excluir cliente')
    try:
        escolha = int(input('Digite a opção desejada: '))
    
        if escolha ==1:
            veiculo.inserir_veiculo()
        elif escolha ==2:
            veiculo.visualizar_veiculos()
        elif escolha ==3:
            veiculo.remover_veiculo()
        elif escolha ==4:
            Cliente.inserir_cliente()
        elif escolha ==5:
            Cliente.visualizar_clientes()
        elif escolha ==6:
            Cliente.excluir_cliente()
        else:
            print("Opção invalida. Tente novamente")

        input('digite Enter para continuar ...')
    except ValueError:
        input("Valor invalido. Tente novamente.")
