produto1 = {} # Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
    #chave    #valor
}
#type(produto)
print(produto) # Todas as chaves (informações) e valores
print(produto['nome']) # printando somente uma chave nome
print(produto['preco']) # printando somente uma chave preco

# alterando o valor
produto['marca'] = "Positivo"
print(produto['marca']) 

# Adicionando chaves
produto ['tela'] = '18"'
print(produto)

# deletando uma chave
del produto['marca']
print(produto)

print(produto.keys()) #chaves
print(produto.values()) #valores
print(produto.items()) #separa tuplas