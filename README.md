# Desafio BEMOBI
## Application for log analysis build with python
A Bemobi precisa de uma aplicação para analisar os logs que contém os registros de mudança de status dos usuários de um novo serviço. Em cada linha do log há um identificador do usuário e seu status (“cancelado” ou “assinado”).

Exemplo de registros encontrados no log:
55211298371229 cancelado

56389428347834 assinado

52211298371229 assinado  

55757575756432 cancelado

56121298371289 cancelado

Os dois primeiros dígitos do identificador do usuário representam seu país de origem:
Brasil - 55
Chile - 56 
México - 52

Seu programa receberá o arquivo de log via stdin, que poderá conter milhares de linhas, e precisará no final do processo gerar um novo arquivo informando as respostas paras as seguintes perguntas:

1 - Quantos usuários usaram o serviço em cada país?
2 - Quantos usuários ativos (cujo último status foi “assinado”) existem em cada país?

Exemplo de resposta esperada no novo arquivo:
Brasil, 2, 0
Chile, 2, 1
México, 1, 1

Onde a primeira coluna identifica o país de origem, a segunda coluna a quantidade de usuários em cada país e a terceira coluna a quantidade de usuários ativos em cada país.

Regras para o exercício numero 2:

Pode ser utilizada, na construção do exercício, a linguagem de programação que você preferir.
O projeto deve conter um README.md com as instruções de como executar o código.
Utilize o Google com sabedoria! Não tenha medo de pesquisar mas não plagie!
Tenha atenção na organização, clareza e elegância do seu código. 
A apresentação no dia da dinâmica será mais voltada para entender como o candidato(a) construiu o código, as dificuldades que teve e lógica utilizada na execução do exercício. 
