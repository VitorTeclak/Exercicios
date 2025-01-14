import os

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
    def visualizar_veiculos():
        try:
            print('1. Para ver lista de motos')
            print('2. Para ver lista de carros')
            print('3. Para ver lista total')
            escolha = int(input('Digite a opção desejada: '))
            if escolha not in [1, 2, 3]:
                raise ValueError

            for veiculo in lista_veiculos:
                if escolha == 1 and veiculo.tipo == 1:
                    if not veiculo in lista_veiculos:
                        print('Não possui motos no estoque')
                    else:
                        clear()
                        print(f'{veiculo.modelo}, Ano: {veiculo.ano}, Quilometragem: {veiculo.quilometragem}, Placa: {veiculo.placa.upper()}, Valor: {veiculo.valor:.3f}')
                elif escolha == 2 and veiculo.tipo == 2:
                    if not veiculo in lista_veiculos:
                        print('Não possui motos no estoque')
                    else:
                        clear()
                        print(f'{veiculo.modelo}, Ano: {veiculo.ano}, Quilometragem: {veiculo.quilometragem}, Placa: {veiculo.placa.upper()}, Valor: {veiculo.valor:.3f}')

                elif escolha == 3:
                    if not veiculo in lista_veiculos:
                        print('Não possui nenhum veiculo no estoque')
                    else:
                        clear()
                        print(f'{veiculo.modelo.upper()}, Ano: {veiculo.ano}, Quilometragem: {veiculo.quilometragem}, Placa: {veiculo.placa.upper()}, Valor: {veiculo.valor:.3f}')

        except ValueError:
            print('Opção inválida.')

    @staticmethod
    def inserir_veiculo():
        clear()
        print('1. Se o veículo for moto')
        print('2. Se o veículo for carro')
        try:
            escolha = int(input('Digite a opção desejada: '))
            if escolha == 1:
                tipo = 'moto'
            elif escolha == 2:
                tipo = 'carro'
            else:
                print('Opção inválida.')
                return

            modelo = input('Digite o modelo do veículo: ')
            ano = int(input('Digite o ano de fabricação: '))
            quilometragem = int(input('Digite a quilometragem do veículo: '))

            while True:
                valor = float(input('Digite o valor do veículo: '))
                if valor <= 0:
                    print('O valor do veículo deve ser maior que 0. Tente novamente.')
                else:
                    break

            while True:
                placa = input('Digite a placa do veículo (7 caracteres): ').strip()
                if len(placa) != 7:
                    print('Placa inválida. Tente novamente.')
                else:
                    break

            novo_veiculo = veiculo(modelo, ano, quilometragem, placa, valor, tipo)
            lista_veiculos.append(novo_veiculo)
            print('Veículo adicionado com sucesso!')
        except ValueError:
            print('Entrada inválida. Tente novamente.')

    @staticmethod
    def remover_veiculo():
        if not lista_veiculos:
            print('Não há veículos no estoque.')
            return

        print('Selecione o veículo a ser removido:')
        for index, veiculo in enumerate(lista_veiculos, 1):
            print(f"{index} - {veiculo.modelo.upper()} - placa:{veiculo.placa.upper()}")

        try:
            escolha = int(input("\nDigite o número do veículo que deseja deletar: "))
            if 1 <= escolha <= len(lista_veiculos):
                veiculo_removido = lista_veiculos.pop(escolha - 1)
                print(f'\nO veículo {veiculo_removido.modelo} foi removido com sucesso.')
            else:
                print('Opção inválida!')
        except (ValueError, IndexError):
            print('Opção inválida. Tente novamente.')

class endereco:
    def __init__ (self, rua,numero, cep, bairro ):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.bairro = bairro

class cliente:
    def __init__(self, nome, cpf,  idade, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
      

    @staticmethod
    def inserir_cliente():
        clear()
        try:
            nome = input('Digite o nome do cliente: ')
            while True:
                cpf = input('Digite o cpf do cliente (Sem pontos): ')
                if not cpf.isdigit() or len(cpf) != 11:
                    print('Quantidade de caracteres invalidos tente novamente.')
                else:
                    break

            idade = int(input('Digite a idade do cliente: '))
            telefone = input('Digite o telefone do cliente (apenas números): ')
            if not telefone.isdigit():
                print('Telefone inválido. Deve conter apenas números.')
                return
            print('')
            print('Dados de endereço')
            print('')
            rua = input('Digite a rua do cliente: ')
            numero = input('Digite o número da casa do cliente: ')
            if not numero.isdigit():
                print('Número inválido. Deve conter apenas números.')
                return
            numero = int(numero)

            cep = input('Digite o CEP do cliente (apenas números): ')
            if not cep.isdigit() or len(cep) != 8:
                print('CEP inválido. Deve conter exatamente 8 dígitos.')
                return

            bairro = input('Digite o bairro do cliente: ')

            endereco_cliente = endereco(rua, numero, cep, bairro)
            novo_cliente = cliente(nome, cpf, idade, telefone, endereco_cliente)
            lista_clientes.append(novo_cliente)
            print(f'\nCliente {novo_cliente.nome} adicionado com sucesso!')

        
        except ValueError:
            print('Valor invalido tente novamente')
    
    @staticmethod
    def visualizar_clientes():
        if not lista_clientes:
            print('Não há clientes na lista.')
        else:
            for cliente in lista_clientes:
                endereco = cliente.endereco
                print(
                    f'Nome: {cliente.nome}, IDADE: {cliente.idade}, CPF: {cliente.cpf}, '
                    f'TELEFONE: {cliente.telefone}, '
                    f'ENDEREÇO: Rua {endereco.rua}, Nº {endereco.numero}, Bairro {endereco.bairro}, CEP: {endereco.cep}'
                )
                








   




    

lista_veiculos = []
lista_clientes = []


print('Seja bem vindo ao sistema da concessionária')

while True:

    clear()
    print('1. Adicionar Veiculo')
    print('2. Visualizar Veiculos')
    print('3. Remover Veiculo')
    print('4. adicionar cliente')
    print('5. Visulizar clientes')
    
    escolha = int(input('Digite a opção desejada: '))

    if escolha ==1:
        veiculo.inserir_veiculo()
    elif escolha ==2:
        veiculo.visualizar_veiculos()
    elif escolha ==3:
        veiculo.remover_veiculo()
    elif escolha ==4:
        cliente.inserir_cliente()
    elif escolha ==5:
        cliente.visualizar_clientes()

    input('digite Enter para continuar ...')
