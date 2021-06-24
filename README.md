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

```
paises = {}
with open('log.txt', 'r') as arquivo:
    for linha in arquivo: # lê o arquivo linha a linha #abre o arquivo linha a linha
        #prefixo, status = linha.rstrip('\n').split() # separa o prefixo e o status (menos eficiente, pois ao dectatar espaços em branco, ValueError é lançado)
        dados = linha.rstrip('\n').split() #separa a linha em números de telefone e status
        if len(dados)!= 2: continue #aqui ocorrer o tratamento para não ocorrer ValueError
        prefixo, status = dados # separa o prefixo e o status
        pais = pais(prefixo) # passa prefixo como referência
```

Nessa parte do código o arquivo é aberto e feito o tratamento para que não ocorra ValueError devido aos espaços em branco que poderia existir no arquivo de log

```
def pais(prefixo):
    if prefixo.startswith('55'):
        return 'Brasil'
    elif prefixo.startswith('56'):
        return 'Chile'
    elif prefixo.startswith('52'):
        return 'Mexico'
    return None
```

Aqui é a função pais recebe o prefixo que é tratado com o método starswith para tratamento de strings. Por fim, retorna o pais com base nos dois digitos iniciais.

```
if pais is not None:
            if pais not in paises:  
                paises[pais] = { 'Total': 0, 'Ativos': 0 }
            paises[pais]['Total'] += 1
            if status == 'assinado':
                paises[pais]['Ativos'] += 1
```
Por fim, temos as condicionais que, caso o pais não esteja no dicionário paises, paises na posição pais, total recebe mais 1 e caso o status seja assinado, o dicionário paises, paises na posição pais ativos, também recebe mais 1.

Obrigado

Antes disso, eu fiz de outra formao mesmo desafio, porém, menos eficiente, que também vou disponibilizar na mesma pasta. É ineficiente pois se o arquivo tiver milhares de linhas, não iria atender ao proposito do desafio.
