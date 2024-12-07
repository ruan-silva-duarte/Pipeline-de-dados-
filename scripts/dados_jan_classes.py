path_dados_a_json = 'data_raw/dados_a.json'
path_dados_b_csv = 'data_raw/dados_b.csv'
path_dados_unidos = 'data_processed/dados_unidos.csv'

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

from Dados import Dados

dados_empresaA = Dados(path_dados_a_json,'json')
dados_empresaB = Dados(path_dados_b_csv,'csv')
print(f'dados empresas A raw {dados_empresaA.dados[0]} \n')
dados_empresaA.manipularJson()
print(f'dados empresas A manipulados {dados_empresaA.dados[0]} \n')
print(f'chaves dados empresa a {dados_empresaA.chaves} \n')
print(f'dados empresa B{dados_empresaB.dados[0]}')
dados_empresaB.renomearCsv(key_mapping)
print(f'dados empresa B após ser renomeado {dados_empresaB.dados[0]}\n')

#união dos dados
dados_fusao = Dados.unirDados(dados_empresaA,dados_empresaB)
print(f'união dos dados primeiro item{dados_fusao.dados[0]}\n')
print(f'união dos dados ultimo item{dados_fusao.dados[-1]}\n')
print(f'qtde dados data fusão {dados_fusao.length}')
print(f'qtde dados empresa A {dados_empresaA.length}')
print(f'qtde dados empresa B {dados_empresaB.length}\n')

#transformando em lista
fusao_dados_em_lista = dados_fusao.listar_dicionário()
print(f'dados em listas{fusao_dados_em_lista[0]}')

#salvando lista
dados_fusao.escreverDados(path_dados_unidos)