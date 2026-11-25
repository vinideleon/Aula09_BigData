#uma empresa precisa organizar uma lista de contatos de cliente para facilitar a comunicação. desenvolva um programa que permita registrar os dados de 3 contatos, informando nome completo, telefone e email
#ao final o sistema deve apresentar todos os contatos cadastrados para consulta.

lista_contato = []

for i in range(3):
    print(f'contato {i+1}')
    contato = {}

    contato['nome'] = input('informe o seu nome completo: ')
    contato['telefone'] = input('informe o seu telefone: ')
    contato['email'] = input('informe o seu email: ')

    lista_contato.append(contato)

for lista in lista_contato:
    print(f'Nome: {lista['nome']}')
    print(f'Telefone: {lista['telefone']}')
    print(f'email: {lista['email']}')