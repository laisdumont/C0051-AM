import pandas as pd


df = pd.read_csv('datasets/traefik.csv')

def quebra_de_recurso(recurso):
    # Função que retorna apenas o primeiro recurso utilizado no acesso

    recurso = recurso.split("/")
    if len(recurso) > 2:
        recurso = recurso[1]
    else: 
        recurso = recurso[0]
    return recurso

def retirar_ponto(ip):
    # Função que retorna o valor do IP somente com números

    ip = ip.replace('.', '')
    return ip

def binarizar_recursos(recurso):
    # Função que classifica recursos existentes como "1" e os inexistentes como "0"

    recursos_validos = ['.well-known', 'Autodiscover', 'avaliacao', 'cgs', 'chaves',
     'cieco', 'cobras', 'computacao', 'cppgi', 'db', 'docs', 'eleicoes', 'evox',
     'facd', 'hestia', 'index.php?s=', 'main', 'mongo', 'pesquisa',
     'phpmyadmin', 'public', 'webapi', 'yoko']

    if recurso in recursos_validos:
        recurso = 1
    else:
        recurso = 0
    return recurso

def tamanho_recurso(dataset):
    dataset['tamanho_recurso'] = 0
    for i in range(len(dataset)):
        dataset.tamanho_recurso[i] = len(dataset.recurso[i])
    return dataset

def binarizar_status(dataset):
    status = ['200', '404', '429']
    for i in range(3):
        dataset[f'status{i}'] = 0
        dataset.loc[dataset['status'] == status[i], f'status{i}'] = 1
    # dataset = dataset.drop(columns=['status'])
    return dataset

def binarizar_metodos(dataset):
    metodos = ['GET', 'HEAD', 'CONNECT', 'OPITIONS', 'PATCH', 'POST', 'PUT']
    for i in range(len(metodos)):
        dataset[f'metodo{i}'] = 0
        dataset.loc[dataset['metodo'] == metodos[i], f'metodo{i}'] = 1
    return dataset

if __name__=="__main__":
    # Remoção de atributos desnecessários
    df = df.drop(columns=['data1'])
    df = df.drop(columns=['data2'])

    df = tamanho_recurso(df)
    df.recurso = df.recurso.apply(quebra_de_recurso)
    df.recurso = df.recurso.apply(binarizar_recursos)

    df = binarizar_status(df)
    df = df[df.status != '-']
    df = df.drop(columns=['status'])

    df = binarizar_metodos(df)
    df = df.drop(columns=['metodo'])

    df.ip = df.ip.apply(retirar_ponto)
    
    df = df.fillna('null')
    
    print(df)
    # df.to_csv('datasets/dadosTratados.csv', index=False)