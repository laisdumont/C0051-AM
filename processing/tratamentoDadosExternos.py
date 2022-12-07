import pandas as pd


df = pd.read_csv('datasets/dataAcessIn.csv')

def quebra_de_recurso(recurso):

    recurso = str(recurso).split(' ')
    return recurso

def retirar_ponto(ip):
    # Função que retorna o valor do IP somente com números

    ip = ip.replace('.', '')
    return ip

def tamanho_recurso(dataset):
    dataset['tamanho_recurso'] = 0
    for i in range(len(dataset)):
        dataset.tamanho_recurso[i] = len(dataset.recurso[i])
    return dataset

def binarizar_status(dataset):
    status = [206, 301, 302, 303, 304, 307, 400, 403, 404]
    for i in range(len(status)):
        dataset[f'status{i}'] = 0
        dataset.loc[dataset['status'] == status[i], f'status{i}'] = 1
    return dataset

def binarizar_metodos(dataset):
    metodos = ['GET', 'HEAD', 'CONNECT', 'PATCH', 'POST']
    for i in range(len(metodos)):
        if i < len(metodos):
            dataset[f'metodo{i}'] = 0
            dataset.loc[dataset['metodo'] == metodos[i], f'metodo{i}'] = 1
    return dataset

def setar_metodo(dataset):
    dataset['metodo'] = 0
    for i in range(len(dataset)):
        df.metodo[i] = df.request[i][:1]
        df.metodo[i] = df.metodo[i][0]
    return dataset

def setar_recurso(dataset):
    dataset['recurso'] = 0
    for i in range(len(dataset)):
        df.recurso[i] = df.request[i][1:2]
        if len(df.recurso[i]) > 0:
            df.recurso[i] = df.recurso[i][0]
        else:
            df.recurso[i] = ''
    return dataset

def binarizar_classe(dataset):
    dataset.loc[dataset['detected'] == 'AMAN', 'detected'] = 1
    dataset.loc[dataset['detected'] == 'DICURIGAI', 'detected'] = 2
    dataset.loc[dataset['detected'] == 'BAHAYA', 'detected'] = 3
    return dataset

if __name__=="__main__":
    # Remoção de atributos desnecessários
    df = df.drop(columns='datetime')
    df = df.drop(columns='gmt')
    df = df.drop(columns='country')
    df = df.drop(columns='browser')
    df = df.drop(columns='referer')
    
    df = binarizar_status(df)
    df = df[df.status != '-']
    df = df.drop(columns=['status'])

    df.request = df.request.apply(quebra_de_recurso)
    
    df = setar_metodo(df)
    df = binarizar_metodos(df)
    
    df = setar_recurso(df)
    df = tamanho_recurso(df)

    df = binarizar_classe(df)

    df = df.drop(columns=['request'])
    df = df.drop(columns=['metodo'])
    df = df.drop(columns=['recurso'])

    df.ip = df.ip.apply(retirar_ponto)
    
    df = df.fillna('null')

    df.loc[df['size'] != int(), 'size'] = 0

    df = df[['ip', 'size', 'status0', 'status1', 'status2', 'status3',
       'status4', 'status5', 'status6', 'status7', 'status8',
       'metodo0', 'metodo1', 'metodo2', 'metodo3', 'metodo4',
       'tamanho_recurso', 'detected']]

    print(df.head())
    # print(df.columns)
    df.to_csv('datasets/dadosExternosTratados.csv', index=False)