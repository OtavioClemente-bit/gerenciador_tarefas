import json
import hashlib
import os
import time

usuario = {} #Função principal

def salvar_usuarios(): #Salvar o usuario
    with open("usuarios.json", "w") as f:
        json.dump(usuario, f, ensure_ascii=False, indent=4)

def carregar_usuarios(): #Carregar o usuario
    global usuario
    try:
        with open("usuarios.json", "r") as f:
            usuario = json.load(f)
    except FileNotFoundError:
        pass

carregar_usuarios()

def limpar_tela(): #Função limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_senha(s): #Segurança da senha
    return hashlib.sha256(s.encode()).hexdigest()

def criar_usuario(): #Função para criar o usuario
    while True:
        limpar_tela()
        print("\u2554" + "\u2550" * 20 + " CRIAR CONTA " + "\u2550" * 20 + "\u2557")
        print("\u2551                                                     \u2551")
        print("\u2551 Digite o nome do usuário:                           \u2551")
        print("\u2551                                                     \u2551")
        print("\u2551         digite 'sair' para voltar ao menu           \u2551")
        print("\u255A" + "\u2550" * 53 + "\u255D")
        print("\033[F" * 4, end="")
        print("\033[C" * 28, end="")
        nome_usuario = input()
        if len(nome_usuario) > 15:
            limpar_tela()
            print("\u2554" + "\u2550" * 28 + "\u2557")
            print("\u2551  Nome de usuario inválido  \u2551")
            print("\u255A" + "\u2550" * 28 + "\u255D")   
            time.sleep(1)
        elif nome_usuario == "sair":
            return nome_usuario
        elif len(nome_usuario) < 5:
            limpar_tela()
            print("\u2554" + "\u2550" * 28 + "\u2557")
            print("\u2551  Nome de usuario inválido  \u2551")
            print("\u255A" + "\u2550" * 28 + "\u255D")   
            time.sleep(1)            
        elif nome_usuario.isalpha():
            if nome_usuario in usuario:
                limpar_tela()
                print("\u2554" + "\u2550" * 33 + "\u2557")
                print("\u2551 Nome de usuário já cadastrado!  \u2551")
                print("\u255A" + "\u2550" * 33 + "\u255D")
                time.sleep(1)
            else:
                return nome_usuario
        else:
            limpar_tela()
            print("\u2554" + "\u2550" * 26 + "\u2557")
            print("\u2551 Nome de usuário inválido \u2551")
            print("\u255A" + "\u2550" * 26 + "\u255D")
            time.sleep(1)

def criar_senha(): #Função para criar a senha
    while True:
        limpar_tela()
        print("\u2554" + "\u2550" * 23 + " CRIAR CONTA " + "\u2550" * 23 + "\u2557")
        print("\u2551                                                           \u2551")
        print("\u2551 Digite a senha para o usuario:                            \u2551")
        print("\u2551                                                           \u2551")
        print("\u2551         digite 'sair' para voltar ao menu                 \u2551")
        print("\u255A" + "\u2550" * 59 + "\u255D")
        print("\033[F" * 4, end="")
        print("\033[C" * 33, end="")
        senha_usuario = input()
        if senha_usuario == "sair":
            break
        elif len(senha_usuario) < 6:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551  Senha muito curta \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)
        elif len(senha_usuario) > 20:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551 Senha muito grande \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)
        else:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551Usuario cadastrado! \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)
            usuario[nome_usuario] = {}
            usuario[nome_usuario]["senha"] = hash_senha(senha_usuario)
            salvar_usuarios()
            break
        


def entrar_usuario(): #Função para entrar no usuario
    while True:
        limpar_tela()
        print("\u2554" + "\u2550" * 25 + " ENTRAR " + "\u2550" * 25 + "\u2557")
        print("\u2551                                                          \u2551")
        print("\u2551 Digite o nome do usuario para entrar:                    \u2551")
        print("\u2551                                                          \u2551")
        print("\u2551         digite 'sair' para voltar ao menu                \u2551")
        print("\u255A" + "\u2550" * 58 + "\u255D")
        print("\033[F" * 4, end="")
        print("\033[C" * 40, end="")
        nome_usuario_login = input()
        if nome_usuario_login == "sair":
            limpar_tela()
            return nome_usuario_login
        elif nome_usuario_login not in usuario:
            limpar_tela()
            print("\u2554" + "\u2550" * 25 + "\u2557")
            print("\u2551  Usuario não encontado  \u2551")
            print("\u255A" + "\u2550" * 25 + "\u255D")
            time.sleep(1)
        else:
            return nome_usuario_login

def verificar_senha(): #Função para verificar a senha
    tentativas = 3
    while True:
        limpar_tela()
        print("\u2554" + "\u2550" * 26 + " ENTRAR " + "\u2550" * 26 + "\u2557")
        print("\u2551                                                            \u2551")
        print("\u2551 Digite a senha do usuario para entrar:                     \u2551")
        print("\u2551                                                            \u2551")
        print("\u2551         digite 'sair' para voltar ao menu                  \u2551")
        print("\u255A" + "\u2550" * 60 + "\u255D")
        print("\033[F" * 4, end="")
        print("\033[C" * 41, end="")
        senha_login = input()
        if hash_senha(senha_login) == usuario[nome_usuario_login]["senha"]:
            limpar_tela()
            print("\u2554" + "\u2550" * 40 + "\u2557")
            print("\u2551                                        \u2551")
            print("\u2551               BEM - VINDO              \u2551")
            print("\u2551                                        \u2551")
            print("\u255A" + "\u2550" * 40 + "\u255D")
            time.sleep(1)
            return nome_usuario_login
        elif senha_login == 'sair':
            break
        else:
            if tentativas == 0:
                limpar_tela()
                print("\u2554" + "\u2550" * 40 + "\u2557")
                print("\u2551 Muitas tentativas, terminal bloqueado! \u2551")
                print("\u255A" + "\u2550" * 40 + "\u255D")
                exit()
            else:
                limpar_tela()
                print("\u2554" + "\u2550" * 48 + "\u2557")
                print(f"\u2551     Senha incorreta. Mais {tentativas} tentativas!        \u2551")
                print("\u255A" + "\u2550" * 48 + "\u255D")
                time.sleep(1.5)
                tentativas -= 1

def menu_principal(): #Menu principal
    while True:
        limpar_tela()
        try:
            print("\u2554" + "\u2550" * 12 + " MENU PRINCIPAL " + "\u2550" * 12 + "\u2557")
            print("\u2551                                        \u2551")
            print("\u2551 1 - CRIAR USUARIO                      \u2551")
            print("\u2551 2 - ENTRAR NO USUARIO                  \u2551")
            print("\u2551 3 - SAIR                               \u2551")
            print("\u2551                                        \u2551")
            print("\u2551 Digite sua escolha:                    \u2551")
            print("\u255A" + "\u2550" * 40 + "\u255D")
            print("\033[F" * 2, end="")
            print("\033[C" * 22, end="")
            menu_escolha = int(input())
            if menu_escolha == 1:
                return menu_escolha
            elif menu_escolha == 2:
                return menu_escolha
            elif menu_escolha == 3:
                return menu_escolha
            else:
                limpar_tela()
                print("\u2554" + "\u2550" * 20 + "\u2557")
                print("\u2551  Entrada invalida  \u2551")
                print("\u255A" + "\u2550" * 20 + "\u255D")
                time.sleep(1)   
        except ValueError:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551  Entrada invalida  \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)  
        
def menu_tarefas(): #Menu das tarefas
        while True:
            limpar_tela()
            try:
                print("\u2554" + "\u2550" * 12 + " MENU PRINCIPAL " + "\u2550" * 12 + "\u2557")
                print("\u2551                                        \u2551")
                print("\u2551 1 - CRIAR TAREFA                       \u2551")
                print("\u2551 2 - LISTAR TAREFAS                     \u2551")
                print("\u2551 3 - CONCLUIR TAREFAS                   \u2551")
                print("\u2551 4 - REMOVER TAREFAS                    \u2551")
                print("\u2551 5 - SAIR                               \u2551")
                print("\u2551                                        \u2551")
                print("\u2551 Digite sua escolha:                    \u2551")
                print("\u255A" + "\u2550" * 40 + "\u255D")
                print("\033[F" * 2, end="")
                print("\033[C" * 22, end="")
                menu_tarefa = int(input())
                if menu_tarefa == 1:
                    return menu_tarefa
                elif menu_tarefa == 2:
                    return menu_tarefa
                elif menu_tarefa == 3:
                    return menu_tarefa
                elif menu_tarefa == 4:
                    return menu_tarefa  
                elif menu_tarefa == 5:
                    return menu_tarefa 
                else:
                    limpar_tela()
                    print("\u2554" + "\u2550" * 20 + "\u2557")
                    print("\u2551  Entrada invalida  \u2551")
                    print("\u255A" + "\u2550" * 20 + "\u255D")
                    time.sleep(1) 
            except ValueError:
                limpar_tela()
                print("\u2554" + "\u2550" * 20 + "\u2557")
                print("\u2551  Entrada invalida  \u2551")
                print("\u255A" + "\u2550" * 20 + "\u255D")
                time.sleep(1)  
              
def criar_tarefas(): #Função para criar as tarefas
    limpar_tela()
    numeraçao = 0
    if "tarefas" not in usuario[nome_usuario_login]:
        usuario[nome_usuario_login]["tarefas"] = []
    else:
        pass 
    print("\u2554" + "\u2550" * 40 + " CRIAR TAREFAS " + "\u2550" * 40 + "\u2557")
    print("\u2551                                                                                               \u2551")
    while True:
        numeraçao += 1
        print(f"\u2551 {numeraçao} -                                                                                           \u2551")
        print("\u2551                                                                                               \u2551")
        print("\u2551 Digite a tarefa que você quer incluir ou digite 'ENTER' para poder retornar ao menu:          \u2551")
        print("\u255A" + "\u2550" * 95 + "\u255D")
        print("\033[F" * 4, end="")
        print("\033[C" * 6, end="")
        tarefa_criada = input()
        if tarefa_criada == "":
            break
        else:
            concluida = "Falta realizar."
            final_tarefa = {"titulo": tarefa_criada, "concluida": concluida}
            usuario[nome_usuario_login]["tarefas"].append(final_tarefa)
            salvar_usuarios()
         
def listar_tarefas(): #Função para listar as tarefas
    limpar_tela()
    enumerar = 0
    print("\u2554" + "\u2550" * 32 + " LISTAR TAREFAS " + "\u2550" * 32 + "\u2557")
    for tarefa in usuario[nome_usuario_login]["tarefas"]:
        enumerar += 1
        titulo_tarefa = tarefa["titulo"].capitalize()
        espacos = 80 - len(f"Tarefa {enumerar} - {titulo_tarefa}")
        if tarefa["concluida"] == "Falta realizar.":
            print(f"\u2551\33[31mTarefa {enumerar} - {titulo_tarefa}\033[0m" + " " * espacos + "\u2551")                  
        else:
            print(f"\u2551\33[32mTarefa {enumerar} - {titulo_tarefa}\033[0m" + " " * espacos + "\u2551")
    print("\u2551                                                                                \u2551")
    print("\u2551Pressione 'ENTER' para voltar ao menu:                                          \u2551")
    print("\u255A" + "\u2550" * 80 + "\u255D")
    print("\033[F" * 2, end="")
    print("\033[C" * 39, end="")
    input()

def marcar_tarefas(): #Função para marcar como concluida as tarefas
    while True:
        limpar_tela()
        enumerar = 0
        print("\u2554" + "\u2550" * 32 + " CONCLUIR TAREFAS " + "\u2550" * 32 + "\u2557")
        for tarefa in usuario[nome_usuario_login]["tarefas"]:
            enumerar += 1
            espacos = 82 - len(f"Tarefa {enumerar} - {tarefa["titulo"].capitalize()} - {tarefa["concluida"].capitalize()}")
            if tarefa["concluida"] == "Falta realizar.": 
                print(f"\u2551\033[31mTarefa {enumerar} - {tarefa["titulo"].capitalize()} - {tarefa["concluida"].capitalize()}\033[0m" + " " * espacos + "\u2551")
            else:
                print(f"\u2551\033[32mTarefa {enumerar} - {tarefa["titulo"].capitalize()} - {tarefa["concluida"].capitalize()}\033[0m" + " " * espacos + "\u2551")
        try:
            print("\u2551                                                                                  \u2551")
            print("\u2551Digite o número da tarefa que você concluiu ou digite 'ZERO' para retornar:       \u2551")
            print("\u255A" + "\u2550" * 82 + "\u255D")
            print("\033[F" * 2, end="")
            print("\033[C" * 77, end="")
            concluir_tarefa = int(input())
            if concluir_tarefa > 0 and concluir_tarefa <= enumerar:
                enumerar = 0
                for tarefa in usuario[nome_usuario_login]["tarefas"]:
                    enumerar += 1
                    if concluir_tarefa == enumerar:
                        if tarefa["concluida"] == "Falta realizar.":
                            tarefa["concluida"] = "Realizada."
                        else:
                            tarefa["concluida"] = "Falta realizar."
                    salvar_usuarios()
            elif concluir_tarefa == 0:
                break
            else:
                limpar_tela()
                print("\u2554" + "\u2550" * 20 + "\u2557")
                print("\u2551  Entrada invalida  \u2551")
                print("\u255A" + "\u2550" * 20 + "\u255D")
                time.sleep(1)   
        except ValueError:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551  Entrada invalida  \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)  

def remover_tarefas(): #Função para remover as tarefas
    while True:
        limpar_tela()
        enumerar = 0
        print("\u2554" + "\u2550" * 35 + " REMOVER TAREFAS " + "\u2550" * 32 + "\u2557")
        for tarefa in usuario[nome_usuario_login]["tarefas"]:
            enumerar += 1
            espacos = 84 - len(f"Tarefa {enumerar} - {tarefa["titulo"].capitalize()} - {tarefa["concluida"].capitalize()}")
            print(f"\u2551Tarefa {enumerar} - {tarefa["titulo"].capitalize()} - {tarefa["concluida"].capitalize()}" + " " * espacos + "\u2551")
        print("\u2551                                                                                    \u2551")
        try:
            print("\u2551Digite o número da tarefa que você deseja remover ou digite 'ZERO' para retornar:   \u2551")
            print("\u255A" + "\u2550" * 84 + "\u255D")
            print("\033[F" * 2, end="")
            print("\033[C" * 83, end="")
            concluir_tarefa = int(input())
            if concluir_tarefa > 0 and concluir_tarefa <= enumerar:
                enumerar = 0
                for tarefa in usuario[nome_usuario_login]["tarefas"]:
                    enumerar += 1
                    if concluir_tarefa == enumerar:
                        usuario[nome_usuario_login]["tarefas"].pop(concluir_tarefa-1)
                        salvar_usuarios()
            elif concluir_tarefa == 0:
                break
            else:
                limpar_tela()
                print("\u2554" + "\u2550" * 20 + "\u2557")
                print("\u2551  Entrada invalida  \u2551")
                print("\u255A" + "\u2550" * 20 + "\u255D")
                time.sleep(1)    
        except ValueError:
            limpar_tela()
            print("\u2554" + "\u2550" * 20 + "\u2557")
            print("\u2551  Entrada invalida  \u2551")
            print("\u255A" + "\u2550" * 20 + "\u255D")
            time.sleep(1)   

while True: #Codigo principal
    menu_escolha = menu_principal() 
    if menu_escolha == 1:
        nome_usuario = criar_usuario()
        if nome_usuario == 'sair':
            pass
        else:
            criar_senha()
    elif menu_escolha == 2:
        nome_usuario_login = entrar_usuario()
        if nome_usuario_login == 'sair':
            pass
        else:
            nome_usuario_login = verificar_senha()
            if nome_usuario_login:
                while True:
                    menu_tarefa = menu_tarefas()
                    if menu_tarefa == 1:
                        criar_tarefas()
                    elif menu_tarefa == 2:
                        listar_tarefas()
                    elif menu_tarefa == 3:
                        marcar_tarefas()
                    elif menu_tarefa == 4:
                        remover_tarefas()
                    elif menu_tarefa == 5:
                        break
    elif menu_escolha == 3:
        limpar_tela()
        print("\u2554" + "\u2550" * 40 + "\u2557")
        print("\u2551                                        \u2551")
        print("\u2551                OBRIGADO                \u2551")
        print("\u2551                                        \u2551")
        print("\u255A" + "\u2550" * 40 + "\u255D")
        exit()
        if menu_escolha == 1:
            criar_tarefas()
        elif menu_escolha == 2: 
            listar_tarefas()
        elif menu_escolha == 3:
            marcar_tarefas()