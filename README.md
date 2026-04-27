'''
FORMATIVA

· Função para salvar lista de estudantes em um arquivo JSON.

· Função para recuperar lista de estudantes de um arquivo JSON e armazenar em uma variável em memória.

· Adaptação das funções de incluir, listar, excluir e editar estudantes para que acessem as duas funções acima sempre que necessário.

Tem como me dar mais detalhes?

Vamos tomar como exemplo o fluxo para incluir um estudante, a seguir o passo a passo das operações pensando nas novas funções para manipulação do arquivo JSON:

1. Leitura dos dados do novo estudante.

2. Criação de um dicionário ou tupla contendo todos os campos informados.

3. Chamada à função para recuperar os dados já cadastrados.

a. A função deve buscar o arquivo de estudantes e retornar a lista recuperada do arquivo (caso o arquivo não exista, retornar uma lista vazia).

4. Adicionar o dicionário ou tupla na lista retornada.

5. Chamada à função para salvar lista de estudantes atualizada.

Deste modo, sempre que incluirmos um novo estudante, já atualizaremos o arquivo que está em disco.

----------------------------------------------------------

SOMATIVA

1. Nível 1: alicerce (persistência e robustez). Esta é a base da nossa aplicação profissional.

a. Persistência de dados com JSON:

i. Ao carregar: antes de iniciar seu loop while True:, você deve tentar ler um arquivo ("portfolio.json", por exemplo). Você deve fazer isso em uma nova função especializada em carregar dados.

1. Use try...except FileNotFoundError: se o arquivo não existir (primeira vez rodando), você simplesmente começa com uma lista de portfólio vazia.

2. Use try...except json.JSONDecodeError: se o arquivo existir, mas estiver vazio ou corrompido, informe esse problema ao usuário e comece com uma lista vazia.

3. Se o try funcionar: carregue os dados do arquivo JSON para sua lista portfólio.

ii. Ao sair: no seu comando QUIT, você deve salvar o estado atual da sua lista portfólio de volta no arquivo. Você deve fazer isso em uma nova função especializada em ler dados.

1. Dica: use json.dump com indent=4 para gerar um arquivo JSON legível e bonito.

b. Robustez com try...except: a sua aplicação não pode mais “crashar”, ou seja, aparecer aquelas mensagens de exceção em vermelho.

i. Dica: procure por todos os input() em seu código nos quais você converte o que o usuário digitou para um número ou um booleano: e se o usuário digitasse um texto qualquer em vez do tipo de dado que você estava esperando? O seu programa deve capturar esse tipo de problema e mostrar uma mensagem amigável, como “ERRO: formato inválido.”

ii. Analise todo o seu código: que tipo de problema você imaginaria que poderia ocorrer? Pense em situações como ler uma lista vazia, um texto que não existe ou um cadastro de um número negativo de projetos. Por exemplo, e se quiséssemos cadastrar -40 projetos no seu código?

c. Continue atualizando o seu diário de bordo.

i. Lembre-se: um dos motivos de termos proposto o diário de bordo (o qual demos detalhes sobre como deve ser a sua criação nas semanas anteriores) é o de entender como foi o seu processo de aprendizagem e determinar a autoria do seu trabalho. Por mais que você tenha realizado de forma totalmente autônoma, crie o seu diário de bordo para que possamos conhecê-lo melhor. A não entrega dele está sujeita ao desconto substancial da nota da atividade somativa 2.

ii. O seu diário de bordo deve atender as especificações da atividade formativa da semana 3.






'''
