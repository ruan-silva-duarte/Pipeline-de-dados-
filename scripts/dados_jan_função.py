import json
import csv

def lerJson(path):
    with open(path,'r') as file:
        dados_json = json.load(file)
        return dados_json

def lerCsv(path):
    new_csv=[]
    with open(path,'r') as file:
        spamReader = csv.DictReader(file)
        for dada in spamReader:
            new_csv.append(dada)
        return new_csv

def lerDados(path,tipo_arquivo):
    if tipo_arquivo == 'json':
        return lerJson(path)
    elif tipo_arquivo == 'csv':
        return lerCsv(path)

def manipularJson(dados_json):
    new_json = []
    for old_dict in dados_json:
        new_dict = {}
        for k, v in old_dict.items():
            if isinstance(v, dict):
                # Desaninhando o dicionário
                for sub_k, sub_v in v.items():
                    new_dict[sub_k] = sub_v  # Prefixo com a chave principal
            elif isinstance(v, list):
                valor_list = ''
                for i, v_list in enumerate(v):  # Usando índice para diferenciar
                    if isinstance(v_list, dict):
                        for v_list_k, v_list_v in v_list.items():
                            # Adicionando o índice para diferenciar as chaves
                            new_dict[f"{v_list_k} {i + 1}"] = v_list_v
                    else:
                        valor_list += f'{str(v_list)} | '
                if valor_list:  # Adiciona a lista como uma string concatenada
                    valor_list = valor_list[:-2]  # Remove o último separador " | "
                    new_dict[k] = valor_list
            else:
                # Caso seja um valor simples
                new_dict[k] = v
        new_json.append(new_dict)
    return new_json

def obterChaves(dados):
    nome_chaves_csv =list(dados[0].keys())
    return nome_chaves_csv

def renomearCsv(new_csv,key_mapping):
    new_csv_renomeado = [] 
    for old_dict in new_csv:
        new_dict = {}
        for dict_k, dict_v in old_dict.items():
            #print(dict_k)
            new_dict[key_mapping[dict_k]] = dict_v
        new_csv_renomeado.append(new_dict)
    return new_csv_renomeado

def unirDados(new_json,new_csv_renomeado):
    data_join = []
    data_join.extend(new_json)
    data_join.extend(new_csv_renomeado)
    return data_join

def transformarDados(nome_colunas,data_join):
    data_join_list = [nome_colunas]
    for old_dict in data_join:
        new_list = []
        for dict_k,dict_v in old_dict.items():
            new_list.append(old_dict.get(dict_k,'indisponível'))
        data_join_list.append(new_list)
    return data_join_list

def escreverDados(path_dados,data_join_list):
    with open(path_dados,'w') as file:
        write = csv.writer(file)
        write.writerows(data_join_list)


#caminho dos dados
path_dados_a_json = 'data_raw/dados_a.json'
path_dados_b_csv = 'data_raw/dados_b.csv'
path_dados_unidos = 'data_processed/dados_unidos.csv'

#mapeamento das chaves
key_mapping={'Código': 'id',
 'Nome do Usuário': 'nome',
 'Idade do Usuário': 'idade',
 'Contato por Email': 'email',
 'Residência': 'rua',
 'Cidade/UF': 'cidade',
 'CEP do Usuário': 'cep',
 'Contato': 'telefone',
 'Habilidades Técnicas': 'habilidades',
 'Empresa 1': 'Empresa 1',
 'Cargo Inicial': 'cargo 1',
 'Data de Início 1': 'inicio 1',
 'Data de Término 1': 'fim 1',
 'Empresa 2': 'empresa 2',
 'Cargo Atual': 'cargo 2',
 'Data de Início 2': 'inicio 2',
 'Data de Término 2': 'fim 2',
 'Status Atual': 'status'}

#atribuindo e validando funções
dados_json = lerDados(path_dados_a_json,'json')
print(f'dados crus json {dados_json[0]}\n')
dados_csv = lerDados(path_dados_b_csv,'csv')
print(f'dados crus csv em json{dados_csv[0]} \n')
new_dados_json = manipularJson(dados_json) 
print(f'novos dados json:{new_dados_json[0]} \n')
chavesCsv = obterChaves(dados_csv)
print(f'as chaves do csv são {chavesCsv} \n')
chavesJson = obterChaves(new_dados_json)
print(f'as chaves do Json são {chavesJson} \n')
new_csv_renomeado = renomearCsv(dados_csv,key_mapping)
print(f'csv renomeado: {new_csv_renomeado[0]} \n')
data_join = unirDados(new_dados_json,new_csv_renomeado)
print(f'dados unidos primeiro item{data_join[0]} \n')
print(f'dados unidos ultimo item{data_join[-1]} \n')
#validando junção
print(f'qtde json {len(new_dados_json)}')
print(f'qtde csv {len(new_csv_renomeado)}')
print(f'qtde join dados {len(data_join)}\n')
#transformando dados em lista
data_join_list = transformarDados(chavesJson,data_join)
print(f'primeiro dado em lista {data_join_list[0]}')
#escrevendo os dados
escreverDados(path_dados_unidos,data_join_list)


