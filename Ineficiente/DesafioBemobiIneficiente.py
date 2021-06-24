def get_pais(prefixo):
    if prefixo.startswith('55'):
        return 'Brasil'
    elif prefixo.startswith('56'):
        return 'Chile'
    elif prefixo.startswith('52'):
        return 'Mexico'
    return None

paises = {}
with open('log.txt', 'r') as arquivo:
    for linha in arquivo: # lê o arquivo linha a linha
        #prefixo, status = linha.rstrip('\n').split() # separa o prefixo e o status
        dados = linha.rstrip('\n').split()
        if len(dados)!= 2: continue
        prefixo, status = dados # separa o prefixo e o status
        pais = get_pais(prefixo)

        if pais is not None:
            if pais not in paises:  
                paises[pais] = { 'Total': 0, 'Ativos': 0 }
            paises[pais]['Total'] += 1
            if status == 'assinado':
                paises[pais]['Ativos'] += 1
    
if __name__=='__main__':
    print(paises)

