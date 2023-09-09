#Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.

##O que seu programa deve conter:

##Um input onde cada interação tenha um texto.
##No final, seu programa deverá ter o output:
##“Olá, Caique! Sua média é: 10 pontos”

print("Olá aluno, para saber a sua media, digite as suas notas:")

nome = input("digite seu nome:")
nota1 = int(input("digite sua primeira nota:"))
nota2 = int(input("digite sua segunda nota:"))
nota3 = int(input("digite sua terceira nota:"))
nota4 = int(input("digite sua quarta nota:"))
media_notas = (nota1 + nota2 + nota3 + nota4)/4



print(f"Olá{nome}! sua média é: {media_notas} pontos.")


