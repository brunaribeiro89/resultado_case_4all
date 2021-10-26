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
for indice_lugar in lista_lugares:
  #posições da lista de lugares(cada posição é um dicionario)
  #print(indice_lugar)
  #limpa o dicionario_categorias
  dicionario_categorias.clear()
  #cria uma lista para armazenar as chaves-categorias
  lista_categoria_keys = list()
  for indice_lista_produto in lista_produtos:
    #posições da lista de produto(cada posição é um dicionario)
    #print(indice_lista_produto)
    for indice_lista_categoria in lista_categorias:
      #posições da lista de categorias(cada posição é um dicionario)
      #print(indice_lista_categoria)
      for indice_produto in indice_lugar["productsId"]:
        #pega  na lista de lugares a chave'productsId' e imprime cada valor dessa lista
        #print(indice_produto)
        if (indice_lista_produto["id"] == indice_produto): #compara o id do produto com a lista de 'productsId'
          for indice_categoria in indice_lista_produto["categoriesId"]:#######fica nesse for ate preencher os produtos dentro das categorias
             #pega  na lista de produtos a chave'categoriesId' e imprime cada valor dessa lista
            #print(indice_categoria)
            if(indice_lista_categoria["id"] == indice_categoria):#compara o id da categoria com a lista de 'categoriesId'
                dicionario_produtos[indice_lista_produto["name"]] = {"preco": (int(indice_lista_produto["price"]) / 100)} 
                print(dicionario_produtos)
                if(indice_lista_categoria["name"] not in lista_categoria_keys):
                  dicionario_categorias[indice_lista_categoria["name"]] = {}
                  print(dicionario_categorias)
                dicionario_categorias[indice_lista_categoria["name"]].update(dicionario_produtos)
                print(dicionario_categorias)
                dicionario_produtos.clear()
                print(dicionario_produtos)
                #retorna a lista de lista_categorias
                lista_categoria_keys = [*dicionario_categorias]
                print( lista_categoria_keys)
  dados_json[indice_lugar["name"]] = (dicionario_categorias.copy())
  print(f'print d_json : {dados_json}')
              #d_jason = {indice_lugar["name"] : {indice_lista_categoria["name"]: {indice_lista_produto["name"]: {"preco": (int(indice_lista_produto["price"]) / 100)}}}}
print(dados_json, type(dados_json)) 
           
              
              
              
      
json.dump(dados_json,file,ensure_ascii = False, indent=4)

file.close()
