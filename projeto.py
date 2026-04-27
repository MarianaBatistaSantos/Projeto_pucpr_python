import datetime
plantas = []
numero_plantas = None

def saber_mais_program():
        print("No momento temos seis comandos: ABOUT, QUIT, ADD, LIST, UPDATE e DELETE.")
        print("ABOUT: Mostra informações sobre o programa.")
        print("QUIT: Encerra o programa.")
        print("ADD: Registrar uma nova planta ao sistema.")
        print("LIST: Listar todos as plantas registradas.")
        print("UPDATE: Atualizar o registro de uma planta já existente.")
        print("DELETE: Deletar o registro de uma planta já existente.")

def about_program():
        print("Este software é um Catálogo Botânico.")
        print("Desenvolvido pela Mariana Batista dos Santos!")
        print("O sistema tem como objetivo registrar plantas, para identificar e classifica-lás.")
        print("Ele é um projeto para a disciplina de Raciocínio Computacional da Pontifícia Universidade Católica do Paraná - PUCPR")   

def quit_program():
        print("Saindo do Catálogo Botânico...")
        print("Até Logo, obrigada!")
        print("-" * 100)
        
def find_plantas(nome_planta_modificar, lista_plantas):
    for nome_planta in lista_plantas: 
            if nome_planta["nome_popular"].upper() == nome_planta_modificar:
                return nome_planta

def voltar_menu():
    print("Voltando ao menu...")
    print("-" * 100)

def add_planta(plantas_add):
        while True:
            try:
                numero_plantas = int(input("Quantas plantas gostaria de registrar? "))
                if numero_plantas <= 0:
                    print("Não é possível cadastrar um número negativo ou zero plantas.")
                    voltar_menu()
                else: 
                    for nome in range(numero_plantas):
                        nome_planta = input(f"Digite o nome popular da planta {nome + 1}: ")
                        nome_planta_cientifico = input(f"Digite o nome científico da planta {nome + 1} | Obs: Caso não saiba ainda apenas escreva um X:")
                        dicionario_plantas = { 
                            "nome_popular": nome_planta,
                            "nome_cientifico": nome_planta_cientifico,
                            "concluido": False,
                            "historico": [ ],
                        }
                        plantas_add.append(dicionario_plantas)
                        print(f"Planta '{nome_planta}' registrada com sucesso!")
                    print("-" * 100)
                if numero_plantas == numero_plantas:
                    print("Todas as plantas foram registradas!")
                break
            except ValueError:
                print("ERRO: Você deve utilizar números, ex: 1,2,3...")
                voltar_menu()
                break

def listar_plantas(plantas_list):
    if len(plantas_list) == 0:
            print("Não há nenhuma planta registrada no momento.")
            voltar_menu()
    else:
        print("Registros de plantas atuais e Detalhes: ")
        print()
        for planta in plantas_list:
            for chave, valor in planta.items():
                print(f"{chave}: {valor}")
            print("-" * 50)
        
print("-" * 100)
print("Olá! Seja bem vindo(a) ao Catálogo Botânico da Mari!!")
print("Caso não saiba os comandos, digite: SABER_MAIS abaixo.")
print("-" * 100)
while True:
    comando = str(input("Digite um comando: ")).upper()
    print("-" * 100)

    if comando == "SABER_MAIS":
        saber_mais_program()
        voltar_menu()
    
    elif comando == "ABOUT":
        about_program()
        voltar_menu()
    
    elif comando == "QUIT":
        quit_program()
        break
    
    elif comando == "ADD":
        add_planta(plantas)
        voltar_menu()
    
    elif comando == "LIST":
        listar_plantas(plantas)
        voltar_menu()
    
    elif comando =="UPDATE":
        nome_atualizar_planta = input("Qual planta você gostaria de modificar? | Obs: Digite o nome popular da planta. ").upper()
        atualizar_planta = find_plantas(nome_atualizar_planta, plantas)
        
        if atualizar_planta is not None:
            atualizar_planta["nome_popular"] =  input("Digite o novo nome popular da planta: ")
            atualizar_planta["nome_cientifico"] = input("Digite o novo nome científico da planta: ")
            atualizar_planta["concluido"] = bool(input("O registro da planta está concluída? Digite 1 para sim e 0 para não: "))
            
            print(f"Planta {atualizar_planta['nome_popular']} atualizada com sucesso!")
            data_mudanca = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tupla_atualizacao = {
                                "DATA": data_mudanca,
                                "NOME_POPULAR": atualizar_planta["nome_popular"], 
                                "NOME_CIENTIFICO": atualizar_planta["nome_cientifico"], 
                                "CONCLUIDO": atualizar_planta["concluido"] 
                                }
            atualizar_planta["historico"].append(tupla_atualizacao)
            voltar_menu()
        else:
            print("Planta não encontrada.")
            voltar_menu()
    
    elif comando =="DELETE":
        nome_deletar_planta = input("Qual registro de planta você gostaria de deletar? | Obs: Digite o nome popular da planta. ").upper()
        deletar_planta = find_plantas(nome_deletar_planta, plantas) 
        if deletar_planta is not None:
            plantas.remove(deletar_planta)
            print(f"Planta {deletar_planta['nome_popular']} removida com sucesso!")
            voltar_menu()

        else:
            print("Planta não encontrada.")
            voltar_menu()
    
    else:
        print("ERRO:Comando não encontrado")
        voltar_menu()