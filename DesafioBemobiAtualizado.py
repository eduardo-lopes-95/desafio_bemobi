with open('log.txt','r') as file:
    arquivo = filter(None, [line.rstrip('\n').split() for line in file])

    prefixo = []
    status = []
    for linha in arquivo:
        prefixo.append(linha[0][:2])
        status.append(linha[1])
    data = list(zip(prefixo, status))

paises = {
    'Brasil': {
        'Total': [p for p in prefixo if p == '55'].count('55'),
        'Ativos': [d[1] for d in data if d[0] == '55' and d[1] == 'assinado'].count('assinado')
    },
    'Chile': {
        'Total': [p for p in prefixo if p == '56'].count('56'),
        'Ativos': [d[1] for d in data if d[0] == '56' and d[1] == 'assinado'].count('assinado')
    },
    'Mexico': {
        'Total': [p for p in prefixo if p == '52'].count('52'),
        'Ativos': [d[1] for d in data if d[0] == '52' and d[1] == 'assinado'].count('assinado')
    }
}
    
print(paises)