projetos = []
numero_projetos = None

while True:
    print("Olá! Seja bem vindo(a) ao Gestor de Planejamento da Mari!!")
    print("Caso não saiba os comandos, digite: SABER_MAIS abaixo.")
    comando = str(input("Digite um comando: ")).upper()
    print("-" * 100)

    if comando == "SABER_MAIS":
        print("No momento temos quatro comandos: ABOUT, QUIT, ADD e LIST.")
        print("ABOUT: Mostra informações sobre o programa.")
        print("QUIT: Encerra o programa.")
        print("ADD: Cadastrar um novo plano ao sistema.")
        print("LIST: Listar todos os planos cadastrados.")
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
                        projetos.append(nome_projeto)
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
            print("Planos atuais: ")
            for i, projeto in enumerate(projetos, start=1):
                print(f"{i}. {projeto}")
                

            print("Voltando ao menu...")
            print("-" * 100)
        

    else:
        print("ERRO:Comando não encontrado")
        print("Voltando ao menu...")
        print("-" * 100)
