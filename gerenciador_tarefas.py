
import os
import time

usuarios = {}  # Dicionário para armazenar usuários, senhas e tarefas

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar_tela()
    print("=============== BEM-VINDO AO GERENCIADOR DE TAREFAS ===============\n")
    print("1. Criar usuário\n2. Entrar com usuário\n3. Sair")
    print("\n==================================================================")
    escolha = input("\nEscolha uma opção: ")

    # --- CRIAR USUÁRIO ---
    if escolha == "1":
        limpar_tela()
        print("=============== CRIAR USUÁRIO ===============\n")
        nome = input("Novo nome de usuário: ").strip()
        if not nome or nome in usuarios:
            print("Nome inválido ou já existente.")
            time.sleep(1.5)
            continue
        senha = input("Senha: ").strip()
        if not senha:
            print("Senha inválida.")
            time.sleep(1.5)
            continue
        usuarios[nome] = {"senha": senha, "tarefas": []}
        print(f"Usuário '{nome}' cadastrado com sucesso!")
        time.sleep(1.5)

    # --- LOGIN ---
    elif escolha == "2":
        limpar_tela()
        print("=============== ENTRAR COM USUÁRIO ===============\n")
        nome = input("Nome de usuário: ").strip()
        if nome not in usuarios:
            print("Usuário não encontrado.")
            time.sleep(1.5)
            continue
        senha = input("Senha: ").strip()
        if senha != usuarios[nome]["senha"]:
            print("Senha incorreta.")
            time.sleep(1.5)
            continue

        # --- MENU DO USUÁRIO ---
        while True:
            limpar_tela()
            print(f"=== MENU DO USUÁRIO: {nome} ===\n1. Adicionar tarefa\n2. Ver tarefas\n3. Remover tarefa\n4. Logout")
            escolha_user = input("Escolha uma opção: ")

            # Adicionar tarefa
            if escolha_user == "1":
                tarefa = input("Digite a nova tarefa: ").strip()
                if tarefa:
                    usuarios[nome]["tarefas"].append(tarefa)
                    print("Tarefa adicionada!")
                else:
                    print("Tarefa inválida.")
                time.sleep(1.5)

            # Ver tarefas
            elif escolha_user == "2":
                limpar_tela()
                tarefas = usuarios[nome]["tarefas"]
                if tarefas:
                    print("=== SUAS TAREFAS ===")
                    for i, t in enumerate(tarefas, 1):
                        print(f"{i}. {t}")
                else:
                    print("Nenhuma tarefa encontrada.")
                input("\nEnter para voltar...")

            # Remover tarefa
            elif escolha_user == "3":
                tarefas = usuarios[nome]["tarefas"]
                if not tarefas:
                    print("Nenhuma tarefa para remover.")
                    time.sleep(1.5)
                    continue
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t}")
                try:
                    idx = int(input("Número da tarefa a remover: "))
                    if 1 <= idx <= len(tarefas):
                        del tarefas[idx - 1]
                        print("Tarefa removida!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
                time.sleep(1.5)

            # Logout
            elif escolha_user == "4":
                break
            else:
                print("Opção inválida.")
                time.sleep(1.5)

    # --- SAIR ---
    elif escolha == "3":
        print("Saindo... Até logo!")
        time.sleep(1)
        break
    else:
        print("Opção inválida.")
        time.sleep(1.5)
