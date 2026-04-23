# Diário de Bordo de IA - Mariana Batista dos Santos 

## 2026/03/26 

### Dificuldade encontrada 
Atualmente, minha dificuldade foi em relação ao uso do comando `for`

### Prompt enviado para a IA 
Estou com dificuldade em relação à funcionalidade, uso e aplicação do comando `for` da linguagem PYTHON. Me explique detalhadamente o uso deste comando, usando exemplos e analogias, me mostre a maioria dos possíveis usos também. (Use a própria documentação do PYTHON como fonte)

### Resposta da IA (Resumo) 
🔁 O que é o for
É um comando que serve para percorrer elementos de uma sequência (lista, string, etc.)

👉 Pense:
“Para cada item dentro de algo, faça isso”

🧩 Estrutura
for variavel in iteravel:
    código

📦 Onde usar
Funciona com:
listas
strings
tuplas
dicionários

🔢 Repetir várias vezes (range)
for i in range(5):
    print(i)

👉 Repete de 0 até 4

⚙️ Usos principais
Percorrer dados
Somar valores
Filtrar (com if)
Contar coisas
Trabalhar com índices (enumerate)

⛔ Comandos importantes
break → para o loop
continue → pula uma volta
pass → não faz nada

🔄 Extras
for com else (executa se não tiver break)
loops dentro de loops
list comprehension (forma mais avançada)

🧠 Ideia principal (da doc do Python)
O for percorre elementos diretamente, sem precisar de contador manual.

📌 Resumo final em uma frase:
👉 for é usado para repetir ações para cada item dentro de uma coleção.

### Minha análise e aprendizado

(Minha dúvida teve como principal objetivo aprender a utilizar o diário, e fixar este conhecimento para usos futuros.)

#### Aprendizado:
 O `for` deve ser utilizado quando for necessário percorrer itens em uma variável ou fazer repetição de um código (utilizando o `range(x)` ),e então realizar uma acão, como armazenar ou classificar.
 `for` são loops finitos,então é possível definir um limite, ao contrário do while, que irá continuar executar o comando indefinidamente até que o objetivo ser cumprido, ou seja, interrompido. 

 #### Análise da IA:
 A resposta atribuida ao diário foi resumida, a orginal continha diversos exemplos em múltiplas situações, separas em níveis, desde o básico até o profissional, prontas para serem executadas com um terminal do CHATGPT. Honestamente, foi muito útil para mim, pois tenho facilidade em aprender com exemplos, logo, foi reforçado um conceito que tenho certeza de que utilizarei no meu desenvolvimento. 

 Um ponto negativo do uso da AI foi que deixe explicitamente a busca no site oficial do PYTHON como fonte de dados, algo que a IA não fez. Porém, entendo que um desenvolvimento melhor do meu PROMPT poderia resolver, sendo sempre importante conferir as informações em sites de confinça.





# Diário de Bordo de IA - Mariana Batista dos Santos 

## 2026/04/10

### Dificuldade encontrada 
O código não estava salvando os projetos dentro da lista

### Prompt enviado para a IA 
Eu gostaria que você explicasse o motivo do meu código não estar armazenando os projetos na lista projetos. (envieio meu código)

### Resposta da IA (Resumo) 
🔴 Onde está o erro?

Dentro do comando "ADD", você fez isso:

lista = []
na_lista = nome_projeto and nome + 1
lista.append(na_lista)

Problemas aqui:
Você criou uma lista nova (lista = []) a cada loop
Ou seja, ela é apagada a cada iteração
E pior: não tem relação nenhuma com projetos
Você nunca usa projetos.append(...)
A lista principal (projetos) continua vazia o tempo todo

Essa linha está errada logicamente:

na_lista = nome_projeto and nome + 1

Isso não cria um "registro" do projeto.
Em Python, isso vai retornar só nome + 1 se nome_projeto não for vazio.

### Minha análise e aprendizado
Bom, eu creio que o erro no código foi ocasionado pela minha falta de atenção, e por ter passado dias sem trabalhar minhas habilidades como programadora, tenho total consciência de que caso eu queira evoluir nas minhas habilidades, eu devo treinar todos os dias SEM FALTA!

O que estava de fato errado era que eu criei uma lista desnecessária (mesmo assim o código iria funcionar) e que ao direcionar os projetos à lista fora do loop, eu estava direcionando à lista errada que estava dentro do loop.

