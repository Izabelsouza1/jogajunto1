
##Mini Case 1: Idade do Pet e Lucro do PETSHOP

#A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro.

#Desafio: Crie um programa Python que calcule a idade de cachorro com base na idade humana.

#O que seu programa deve conter:

#solicitar ao usuário a idade humana do pet (um número inteiro).
#Calcular a idade do pet, levando em consideração que cada ano da idade humana corresponde a 7.
#Exibir a idade do pet ao usuário.
#Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro.

##Valores por banho X Custo por banho

#Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
#Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
#Cachorro de médio porte: BANHO: R$50,00 | CUSTO: R$5,00

### Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com este animal foi de R$550,00

idade_do_pet = int(input("digite a idade do seu pet:"))
idade_do_pet_humano = idade_do_pet * 7

print(f"A idade do seu Pet em anos humanos é aproximadamente:{idade_do_pet_humano}" )
