import os
import datetime

agenda = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_tarefa():
    clear()
    nome_tarefa = input('Digite o nome da tarefa a ser adicionada: ')
    tarefa = input('Escreva a tarefa a ser adicionada: ')
    data_prevista = input('Digite a data a ser concluída (dd/mm/yyyy): ')
    print(f'A tarefa "{nome_tarefa}" foi adicionada com sucesso!')
    agenda[nome_tarefa] = {
        'tarefa': tarefa,
        'data_prevista': data_prevista
    }

def visualizar_tarefas():
    clear()
    if not agenda:
        print('Você não possui anotações na sua agenda.')
    else:
        print('Agenda atual:')
        for nome_tarefa, dados in agenda.items():
            print(f'Tarefa: {nome_tarefa}, Descrição: {dados["tarefa"]}, Data prevista de conclusão: {dados["data_prevista"]}')

def editar_tarefa():
    clear()
    if not agenda:
        print("Não há tarefas para editar.")
        return
    print("Escolha uma tarefa para editar:")
    for index, nome_tarefa in enumerate(agenda, 1):
        print(f"{index} - {nome_tarefa}")
    try:
        escolha_tarefa = int(input("\nDigite o número da tarefa que deseja editar: "))
        nome_tarefa_selecionada = list(agenda.keys())[escolha_tarefa - 1]
    except (ValueError, IndexError):
        print("Opção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")
        return
    print(f"\nVocê escolheu a tarefa: {nome_tarefa_selecionada}")
    print("1 - Mudar o nome da tarefa")
    print("2 - Mudar a descrição da tarefa")
    print("3 - Mudar a data de conclusão")
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        novo_nome = input('Digite o novo nome para a tarefa: ')
        agenda[novo_nome] = agenda.pop(nome_tarefa_selecionada)
        print(f'Nome da tarefa alterado para "{novo_nome}".')
    elif escolha == '2':
        nova_descricao = input('Digite a nova descrição para a tarefa: ')
        agenda[nome_tarefa_selecionada]['tarefa'] = nova_descricao
        print(f'Descrição da tarefa "{nome_tarefa_selecionada}" foi alterada.')
    elif escolha == '3':
        nova_data_str = input('Digite a nova data de conclusão (dd/mm/yyyy): ')
        try:
            datetime.datetime.strptime(nova_data_str, '%d/%m/%Y')
            agenda[nome_tarefa_selecionada]['data_prevista'] = nova_data_str
            print(f'A data de conclusão da tarefa "{nome_tarefa_selecionada}" foi alterada.')
        except ValueError:
            print("Data inválida! Por favor, use o formato dd/mm/yyyy.")

def concluir_tarefa():
    if not agenda:
        print('Não há tarefas a serem concluídas.')
        return
    print('Selecione a tarefa a ser concluída:')
    for index, nome_tarefa in enumerate(agenda, 1):
        print(f"{index} - {nome_tarefa}")
    try:
        escolha_tarefa = int(input("\nDigite o número da tarefa que deseja concluir: "))
        nome_tarefa_selecionada = list(agenda.keys())[escolha_tarefa - 1]
    except (ValueError, IndexError):
        print("Opção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")
        return
    print(f"Tem certeza que deseja concluir a tarefa: {nome_tarefa_selecionada}?")
    print("1 - Sim")
    print("2 - Não")
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        del agenda[nome_tarefa_selecionada]
        print(f'A tarefa "{nome_tarefa_selecionada}" foi concluída e removida da lista.')
    elif escolha == '2':
        print('Voltando ao menu principal.')
    else:
        print('Opção inválida.')

def excluir_tarefa():
    if not agenda:
        print('Não há tarefas a serem excluídas.')
        return
    print('Selecione a tarefa a ser excluída:')
    for index, nome_tarefa in enumerate(agenda, 1):
        print(f"{index} - {nome_tarefa}")
    try:
        escolha_tarefa = int(input("\nDigite o número da tarefa que deseja excluir: "))
        nome_tarefa_selecionada = list(agenda.keys())[escolha_tarefa - 1]
    except (ValueError, IndexError):
        print("Opção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")
        return
    print(f"Tem certeza que deseja excluir a tarefa: {nome_tarefa_selecionada}?")
    print("1 - Sim")
    print("2 - Não")
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        del agenda[nome_tarefa_selecionada]
        print(f'A tarefa "{nome_tarefa_selecionada}" foi excluída.')
    elif escolha == '2':
        print('Voltando ao menu principal.')
    else:
        print('Opção inválida.')

print('Seja bem-vindo à sua agenda pessoal!')
while True:
    clear()
    print('1 - Adicionar nova tarefa')
    print('2 - Visualizar tarefas')
    print('3 - Editar tarefa')
    print('4 - Concluir tarefa')
    print('5 - Excluir tarefa')
    print('6 - Sair')
    try:
        escolha = int(input('Digite a opção desejada: '))
        if escolha == 1:
            adicionar_tarefa()
        elif escolha == 2:
            visualizar_tarefas()
        elif escolha == 3:
            editar_tarefa()
        elif escolha == 4:
            concluir_tarefa()
        elif escolha == 5:
            excluir_tarefa()
        elif escolha == 6:
            print('Saindo da agenda. Até mais!')
            break
        else:
            print('Número inválido. Tente novamente.')
    except ValueError:
        print('Opção inválida. Por favor, digite um número.')
    input('Pressione ENTER para continuar...')
