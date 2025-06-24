import os
import time
usuarios = {} # Dicionário para armazenar usuários e senhas}
def limpar_tela(): # Função para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    limpar_tela()
    print("=============== BEM-VINDO AO GERENCIADOR DE TAREFAS ===============\n")
    print("1. Criar usuário\n" \
        "2. Entrar com usuário\n" \
        "3. Sair")
    print("\n==================================================================")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1": # Criar usuário
        limpar_tela()
        print("=============== CRIAR USUÁRIO ===============\n")
        nome = input("Novo nome de usuário: ")
        if nome in usuarios:
            limpar_tela()
            print("Já existe um usuário com esse nome.")
            time.sleep(1)
            limpar_tela()
        elif nome.strip() == "":
            limpar_tela()
            print("Nome de usuário inválido. Tente novamente.")
            time.sleep(1)
            limpar_tela()
        else:
            senha = input("Senha: ")
            usuarios[nome] = {"senha": senha, "tarefas": []}
            if senha.strip() == "":
                limpar_tela()
                print("Senha inválida. Tente novamente.")
                time.sleep(1)
                limpar_tela()
            else:
                limpar_tela()
                print(f"\nUsuário '{nome}' cadastrado com sucesso!")
                time.sleep(1)
                limpar_tela()
    elif escolha == "2":
        limpar_tela()
        print("=============== ENTRAR COM USUÁRIO ===============\n")
        nome = input("Nome de usuário: ")
        if nome not in usuarios:
            limpar_tela()
            print("Usuário não encontrado. Tente novamente.")
            time.sleep(1)
            limpar_tela()
        else:
            senha = input("Senha: ")
            if senha == usuarios[nome]["senha"]:
                limpar_tela()
                print(f"Bem-vindo, {nome}!")
                while True:
                    print("=============== MENU ===============\n"     "1. Adicionar tarefa\n"     "2. Ver tarefas\n"     "3. Remover tarefa\n"     "4. Sair")
                    print("====================================")
                    escolha = input("Escolha uma opção: ")
                    if escolha == "1": # Adicionar tarefa
                        limpar_tela()
                        print("=============== ADICIONAR TAREFA ===============\n")
                        tarefa_nova = input("Digite a tarefa: ")
                        if tarefa_nova.strip() == "":
                            limpar_tela()
                            print("Tarefa inválida. Tente novamente.")
                            time.sleep(1)
                            limpar_tela()
                        else:
                            usuarios[nome]["tarefas"].append(tarefa_nova)
                            limpar_tela()
                            print("Tarefa adicionada com sucesso!")  
                            time.sleep(1)
                            limpar_tela()  
                    elif escolha == "2": # Ver tarefas
                        limpar_tela()
                        if usuarios[nome]["tarefas"]:
                            print("=============== TAREFAS ===============\n")
                            for i in range(len(usuarios[nome]["tarefas"])):
                                print(f"Tarefa {i + 1}: {usuarios[nome]["tarefas"][i]}")
                            print("\n=======================================")
                            input("\nPressione Enter para voltar ao menu...")
                            limpar_tela()
                        else:
                            limpar_tela()
                            print("Nenhuma tarefa encontrada.")
                            input("\nPressione Enter para voltar ao menu...")
                            limpar_tela()
                    elif escolha == "3": # Remover tarefa
                        limpar_tela()
                        if usuarios[nome]["tarefas"]:
                            print("=============== REMOVER TAREFA ===============\n")
                            for i in range(len(usuarios[nome]["tarefas"])):
                                print(f"Tarefa {i + 1}: {usuarios[nome]["tarefas"][i]}")
                            print("\n========================================")
                            try:
                                numero = int(input("Digite o número da tarefa que deseja remover: "))
                                if 1 <= numero <= len(usuarios[nome]["tarefas"]):
                                    del usuarios[nome]["tarefas"][numero - 1]
                                    limpar_tela()
                                    print("Tarefa removida com sucesso!")
                                    time.sleep(1)
                                    limpar_tela()
                                else:
                                    limpar_tela()
                                    print("Número inválido. Tente novamente.")
                                    time.sleep(2)
                                    limpar_tela()
                            except ValueError:
                                limpar_tela()
                                print("Opção inválida. Tente novamente.")
                                time.sleep(2)
                                limpar_tela()
                        else:
                            limpar_tela()
                            print("Nenhuma tarefa encontrada.")
                            input("\nPressione Enter para voltar ao menu...")
                            limpar_tela()
                    elif escolha == "4": # Sair do programa
                        limpar_tela()
                        print("=============== OBRIGADO ===============\n")
                        print("Saindo do programa...")
                        print("\n========================================")
                        break
                    else: 
                        limpar_tela()
                        print("Opção inválida. Tente novamente.")
                        time.sleep(2)
                        limpar_tela()
            else:
                print("Senha incorreta. Tente novamente.")
                time.sleep(1)
                limpar_tela()
    elif escolha == "3":
        limpar_tela()
        print("=============== OBRIGADO ===============\n")
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        limpar_tela()
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        limpar_tela()

        
        



        
