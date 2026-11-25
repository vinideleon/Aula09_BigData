# uma livraria esta organizando seu catalogo e precisa registrar informações sobre alguns livros. desenvolva um programa, que permita cadastrar os dados de 3 livros, informando titulo, autor, ano, genero, paginas

lista_catalogo = []

for i in range(3):
    print(f'\nlivro {i+1}')
    livro = {}

    livro['titulo'] = input('informe o nome do livro: ')
    livro['autor'] = input('informe o nome do autor: ')
    livro['ano'] = int(input('informe o ano de publicação: '))
    livro['genero'] = input('informe o genero do livro: ')
    livro['paginas'] = int(input('informe o numero de paginas: '))
    
    lista_catalogo.append(livro)

#print(lista_catalogo)
for elemento in lista_catalogo: # 3 vezes
    # print(elemento)
    if elemento['ano'] >= 2020:
        print(elemento)
        print(f'Nome: {elemento['titulo']}')
        print(f'Ano: {elemento['ano']}')