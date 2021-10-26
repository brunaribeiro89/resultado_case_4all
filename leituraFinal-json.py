import json

file = open('data.json', 'rb')
data = json.load(file)

#print(data)

#criar listas para armazenar os 3 objetos
lista_produtos = []
lista_categorias = []
lista_lugares = []
lista_todos_valores = []
#criar dicionarios 
dados_json = dict()
dicionario_categorias = dict()
dicionario_produtos = dict()


for indice in data['products']:
  lista_produtos.append(indice)
print(f'lista_produtos: {lista_produtos}')
print()

for indice in data['categories']:
  lista_categorias.append(indice)
print(f'lista_categorias: {lista_categorias}')
print()


for indice in data['establishments']:
  lista_lugares.append(indice)
print(f'lista_lugares: {lista_lugares}')
print()


file.close()

file = open('result.json', 'w', encoding='UTF-8')




#lógica final do código
for indice_lugar in lista_lugares: #pega posições da lista de lugares(cada posição é um dicionario)
  dicionario_categorias.clear()#limpa o dicionario_categorias
  lista_categoria_keys = list()#cria uma lista para armazenar as chaves-categorias
  for indice_lista_produto in lista_produtos:#pega posições da lista de produto(cada posição é um dicionario)
    for indice_lista_categoria in lista_categorias:#pega posições da lista de categorias(cada posição é um dicionario) 
      for indice_produto in indice_lugar["productsId"]: #pega  na lista de lugares a chave'productsId' e imprime cada valor dessa lista
        if (indice_lista_produto["id"] == indice_produto): #compara o id do produto com a lista de 'productsId'
          for indice_categoria in indice_lista_produto["categoriesId"]: #pega  na lista de produtos a chave'categoriesId' e imprime cada valor dessa lista 
            ##fica nesse for ate preencher os produtos dentro das categorias
            if(indice_lista_categoria["id"] == indice_categoria):#compara o id da categoria com a lista de 'categoriesId'
                dicionario_produtos[indice_lista_produto["name"]] = {"price": (int(indice_lista_produto["price"]) / 100)} 
                print(dicionario_produtos)
                if(indice_lista_categoria["name"] not in lista_categoria_keys):
                  dicionario_categorias[indice_lista_categoria["name"]] = {}
                  print(dicionario_categorias)
                dicionario_categorias[indice_lista_categoria["name"]].update(dicionario_produtos)
                print(dicionario_categorias)
                dicionario_produtos.clear()
                #print(dicionario_produtos)
                lista_categoria_keys = [*dicionario_categorias] #retorna a lista de lista_categorias
                #print( lista_categoria_keys)
  dados_json[indice_lugar["name"]] = (dicionario_categorias.copy())
  #print(dados_json)
print(dados_json, type(dados_json)) 
           
                      
              
      
json.dump(dados_json,file,ensure_ascii = False, indent=4)

file.close()
