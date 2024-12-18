import os

estoque = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_produto():
    clear()
    nome = input('Digite o nome do produto: ')
    qtd = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço do produto: '))

    if nome in estoque:
        estoque[nome]['quantidade'] += qtd  
    else:
        estoque[nome] = {'quantidade': qtd, 'preço': preco}  

    print(f"Produto '{nome}' adicionado com sucesso!")

def consultar_estoque():
    clear()
    if not estoque:
        print("Estoque vazio.")
    else:
        print("Estoque Atual:")
        for nome, dados in estoque.items():
            print(f"- {nome}: {dados['quantidade']} unidades, R$ {dados['preço']:.2f} cada")

def excluir_produto():
    clear()
    nome = input('digite o nome do produto a ser excluido: ')
    if nome in estoque:
        del estoque[nome]
        print(f"O produto '{nome}' foi excluído do estoque.")
    else:
        print(f"O produto '{nome}' não existe no estoque.")

def vender_produto():
    clear()

    nome = input('digite o nome do produto')
    if nome in estoque:
        try:
            qtd = int(input('Digite a quantidade que irá vender: '))
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro.")
            return

        if qtd <= 0:
            print("A quantidade deve ser maior que zero. Tente novamente.")
            return

        if qtd > estoque[nome]['quantidade']:
            print(f"A quantidade digitada ({qtd}) é maior que a quantidade em estoque ({estoque[nome]['quantidade']}). Tente novamente.")
            return
        estoque[nome]['quantidade'] -= qtd

        if estoque[nome]['quantidade'] == 0:
            del estoque[nome]
            print(f"Produto '{nome}' vendido e removido do estoque com sucesso!")
        else:
            print(f"Produto '{nome}' vendido com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def mostrar_total():
    clear()
    if not estoque: 
        print("Estoque vazio.")
    else:
        total = 0  
        print("Estoque Atual:")
        for nome, dados in estoque.items():
            subtotal = dados['preço'] * dados['quantidade'] 
            total += subtotal
            print(f"- {nome}: {dados['quantidade']} unidades, Preço unitário: R$ {dados['preço']:.2f}, Subtotal: R$ {subtotal:.2f}")
        
        print(f"\nO valor total do estoque é: R$ {total:.2f}")

while True:
    clear()
    print('1. adicioar produto')
    print('2. consultar estoque')
    print('3. excluir produto')
    print('4. vender produto')
    print('5. mostrar total')
    print('6. Sair')
    escolha = int(input('digite a função desejada: '))

    if escolha == 1:
        adicionar_produto()
    elif escolha == 2:
        consultar_estoque()
    elif escolha == 3:
        excluir_produto()
    elif escolha == 4:
        vender_produto()
    elif escolha == 5:
        mostrar_total()
    elif escolha == 6:
        break
    else: 
        print('digite uma opção valida')

    input('digite enter para continuar...')
