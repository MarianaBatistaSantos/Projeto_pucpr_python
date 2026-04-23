
import datetime

projetos = [ ]
numero_projetos = None




while True:
    print("Olá! Seja bem vindo(a) ao Gestor de Planejamento da Mari!!")
    print("Caso não saiba os comandos, digite: SABER_MAIS abaixo.")
    comando = str(input("Digite um comando: ")).upper()
    print("-" * 100)




    if comando == "SABER_MAIS":
        print("No momento temos seis comandos: ABOUT, QUIT, ADD, LIST, UPDATE e DELETE.")
        print("ABOUT: Mostra informações sobre o programa.")
        print("QUIT: Encerra o programa.")
        print("ADD: Cadastrar um novo plano ao sistema.")
        print("LIST: Listar todos os planos cadastrados.")
        print("UPDATE: Atualizar um plano já existente.")
        print("DELETE: Deletar um plano já existente.")
        print("Voltando ao menu...")
        print("-" * 100)
              




    elif comando == "ABOUT":
        print("Este software é um Gestor de Planejamento, desenvolvido pela Mariana Batista dos Santos!\nO sistema tem como objetivo auxiliar no planejamnto da vida, seja pessoal ou profissional")
        print("Ele é um projeto para a disciplina de Raciocínio Computacional da Pontifícia Universidade Católica do Paraná - PUCPR")
        print("Voltando ao menu...")
        print("-" * 100)




    elif comando == "QUIT":
        print("Saindo do Gestor de Planejamento...")
        print("Até Logo, obrigada!")
        print("-" * 100)
        break







    elif comando == "ADD":
        while True:
            try:
                numero_projetos = int(input("Quantos planos gostaria de cadastrar? "))

                if numero_projetos <= 0:
                    print("Não é possível cadastrar um número negativo ou zero planos.")
                    print("Voltando ao menu...")
                    print("-" * 100)
                else: 
                    for nome in range(numero_projetos):
                        nome_projeto = input(f"Digite o nome do plano {nome + 1}: ")


                        dicionario_planos = { 
                            "nome": nome_projeto,
                            "concluido": False,
                            "historico": [],
                        }
                        projetos.append(dicionario_planos)

                        print(f"Projeto '{nome_projeto}' cadastrado com sucesso!")
                    print("-" * 100)

                if numero_projetos == numero_projetos:
                    print("Todos os planos foram cadastrados!")
                    print("Voltando ao menu...")
                print("-" * 100)
                break

            except ValueError:
                print("ERRO: Você deve utilizar números, ex: 1,2,3...")
                print("Voltando ao menu...")
                print("-" * 100)
                break





    elif comando == "LIST":
        if len(projetos) == 0:
            print("Não há nenhum plano cadastrado no momento.")
            print("Voltando ao menu...")
            print("-" * 100)


        else:
            print("Planos atuais e Detalhes: ")
            print()
            for projeto in projetos:

                for chave, valor in projeto.items():
                    print(f"{chave}: {valor}")
                print("-" * 50)
                

            print("Voltando ao menu...")
            print("-" * 100)


    elif comando =="UPDATE":
        nome_atualizar_plano = input("Qual plano você gostaria de modificar? ")
        atualizar_plano = None
        for plano in projetos: 
            if plano["nome"] != nome_atualizar_plano: 
                continue
            atualizar_plano = plano
            break
        if atualizar_plano is not None:
            nome = input("Digite o novo nome do plano: ")
            status = bool(input("O plano está concluído? Digite 1 para sim e 0 para não: "))
            print(f"Plano {atualizar_plano['nome']} atualizado com sucesso!")

            atualizar_plano["nome"] = nome 
            atualizar_plano["concluido"] = status
            data_mudanca = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            tupla_atualizacao =(data_mudanca ,atualizar_plano["nome"], atualizar_plano["concluido"] )
            atualizar_plano["historico"].append(tupla_atualizacao)

            print("Voltando ao menu...")
            print("-" * 100)


        else:
            print("Plano não encontrado.")
            print("Voltando ao menu...")
            print("-" * 100)


    elif comando =="DELETE":

        nome_deletar_plano = input("Qual plano você gostaria de deletar? ").upper()
        deletar_plano = None

        for plano in projetos: 
            if plano["nome"].upper() != nome_deletar_plano: 
            
                continue

            deletar_plano = plano
            break

        if deletar_plano is not None:
            projetos.remove(deletar_plano)
            print(f"Plano {deletar_plano['nome']} removido com sucesso!")



            print("Voltando ao menu...")
            print("-" * 100)

        else:
            print("Plano não encontrado.")
            print("Voltando ao menu...")
            print("-" * 100)

    else:
        print("ERRO:Comando não encontrado")
        print("Voltando ao menu...")
        print("-" * 100)
