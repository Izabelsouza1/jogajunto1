##Crie um script com as seguintes instruções, pesquisando na internet como fazer:

#Crie uma tupla com 5 dados
#Altere a tupla para uma lista
#Insira 2 dados extras a essa lista
#Remova o primeiro dado da lista
#Remova o último dado da lista
#Faça um print com o primeiro dado da lista
#Faça um print com a quantidade de dados da lista
#Crie um dicionário com os seguintes dados:
#Nome, Idade, Profissão
#Imprima somente o valor contido na chave Nome do dicionário


#Crie uma tupla com 5 dados:
cidades_de_pernambuco = ("Recife", "carpina", "Lagoa de Itaenga", "paulista")

#Altere a tupla para uma lista
lista_cidades_de_pernambuco = list(cidades_de_pernambuco)


#Insira 2 dados extras a essa lista:
lista_cidades_de_pernambuco.append("Limoeiro")
lista_cidades_de_pernambuco.append("Camaragibe")

#Remova o primeiro dado da lista:
lista_cidades_de_pernambuco.remove ("Recife")

#Remova o último dado da lista:
lista_cidades_de_pernambuco.remove ("Camaragibe")

#Faça um print com o primeiro dado da lista:
print(lista_cidades_de_pernambuco[0])

#Faça um print com a quantidade de dados da lista:
print(len(lista_cidades_de_pernambuco))


#Crie um dicionário com os seguintes dados:
#Nome, Idade, Profissão
meu_dicionario = {
    "nome": "Maria",
    "idade": 20,
    "profissão": "Enfermeira"
}

#Imprima somente o valor contido na chave Nome do dicionário:
print(meu_dicionario["nome"])