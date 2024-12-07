import json
import csv

class Dados:

    def __init__(self,path,tipo_arquivo):
        self.path = path
        self.tipo_arquivo = tipo_arquivo
        self.dados = self.lerDados()
        self.chaves = self.obterChaves()
        self.length = self.contarQtde()

    def lerJson(self):
        with open(self.path,'r') as file:
            dados_json = json.load(file)
        return dados_json
    
    def lerCsv(self):
        new_csv=[]
        with open(self.path,'r') as file:
            spamReader = csv.DictReader(file)
            for dada in spamReader:
                new_csv.append(dada)
            return new_csv
        
    def lerDados(self):
        if self.tipo_arquivo == 'json':
            return self.lerJson()
        elif self.tipo_arquivo == 'csv':
            return self.lerCsv()
        elif self.tipo_arquivo == 'list':
            dados=self.path
            self.path = 'lista em memória'
        return dados
        
    def manipularJson(self):
        new_json = []
        for old_dict in self.lerDados():
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
        self.dados = new_json

    def obterChaves(self):
            nome_chaves_csv =list(self.dados[0].keys())
            return nome_chaves_csv
    
    def contarQtde(self):
        qtdeDados = len(self.dados)
        return qtdeDados

    def renomearCsv(self,key_mapping):
        new_csv_renomeado = [] 
        for old_dict in self.dados:
            new_dict = {}
            for dict_k, dict_v in old_dict.items():
                #print(dict_k)
                new_dict[key_mapping[dict_k]] = dict_v
            new_csv_renomeado.append(new_dict)
        self.dados = new_csv_renomeado

    def unirDados(dados1,dados2): #pedir a instancia dados de cada empresa
        data_join = []
        data_join.extend(dados1.dados) #instancia.dados
        data_join.extend(dados2.dados) #instancia.dados
        return Dados(data_join,'list') #retorna uma instancia para obter os construtores e vai salvar .dados com o data_join
    
    def listar_dicionário(self):
        data_join_list = [self.chaves]
        for old_dict in self.dados:
            new_list = []
            for dict_k,dict_v in old_dict.items():
                new_list.append(old_dict.get(dict_k,'indisponível'))
            data_join_list.append(new_list)
        return data_join_list
    
    def escreverDados(self,path_dados):
        with open(path_dados,'w') as file:
            write = csv.writer(file)
            write.writerows(self.listar_dicionário())