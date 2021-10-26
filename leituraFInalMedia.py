import json

file = open('data.json', 'rb')
data = json.load(file)

#print(data)

#criar listas para armazenar os 3 objetos
lista_produtos = []
lista_categorias = []
lista_lugares = []
lista_todos_valores = []
lista_produtos_price = []
#criar dicionarios 
dados_json = dict()
dicionario_categorias = dict()
dicionario_produtos = dict()
dicionario_produtos_price = dict()



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

file = open('resultAvg.json', 'w', encoding='UTF-8')


'''for indice_lugar in lista_lugares:
  #vai na lista_lugares e imprime as posições(cada posição é um dicionario)
  #print(f' conteudo das posicoes da lista_lugares : {indice_lugar}' )
  for indice_produto in indice_lugar["productsId"]:
    #vai em cada posição(cada posição é um dicionario) da lista_lugares e procura pela chave productsId e imprime os valores de id
    #print(f'valores da chave productsId : {indice_produto}')
    for indice_lista_categoria in lista_categorias:
     for indice_lista_produto in lista_produtos:  
      #for indice_lista_categoria in lista_categorias:
        #print(f' conteudo das posicoes da lista_produtos : {indice_lista_produto}')
        if (indice_lista_produto["id"] in indice_lugar["productsId"]) and (indice_lista_categoria["id"] in indice_lista_produto["categoriesId"] ):
          d_jason = {indice_lugar["name"] : {indice_lista_categoria["name"]: {indice_lista_produto["name"]: {"preco": (int(indice_lista_produto["price"]) / 100)}}}}
          print(d_jason, type(d_jason))'''

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
          for indice_categoria in indice_lista_produto["categoriesId"]:
             #pega  na lista de produtos a chave'categoriesId' e imprime cada valor dessa lista
            #print(indice_categoria)
            if(indice_lista_categoria["id"] == indice_categoria):#compara o id da categoria com a lista de 'categoriesId'
                dicionario_produtos[indice_lista_produto["name"]] = {"preco": (int(indice_lista_produto["price"]) / 100)} 
                print(dicionario_produtos)
                if(indice_lista_categoria["name"] not in lista_categoria_keys):
                  dicionario_categorias[indice_lista_categoria["name"]] = {}
                  lista_produtos_price.append(int(indice_lista_produto["price"]) / 100)
                  print(dicionario_categorias)
                dicionario_categorias[indice_lista_categoria["name"]].update(dicionario_produtos)
                print(dicionario_categorias)
                dicionario_produtos.clear()
                #retorna a lista de lista_categorias
                lista_categoria_keys = [*dicionario_categorias]
                print( lista_categoria_keys)
  soma = 0 
  for valores in lista_produtos_price:
    soma = soma + valores
  dicionario_produtos_price["avgPrice"] = (soma/len(lista_produtos_price))#acresccento a nova chave 'avgPrice'
  dados_json[indice_lugar["name"]] = (dicionario_categorias.copy())
  dados_json[indice_lugar["name"]].update(dicionario_produtos_price)
  print(dados_json)
              #d_jason = {indice_lugar["name"] : {indice_lista_categoria["name"]: {indice_lista_produto["name"]: {"preco": (int(indice_lista_produto["price"]) / 100)}}}}
print(dados_json, type(dados_json)) 
           
                      
              
      
json.dump(dados_json,file,ensure_ascii = False, indent=4)

file.close()
