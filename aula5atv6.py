#Mini Case 3: Operações de teste

##Imagine que você está em um processo se seleção para ocupar uma vaga de QA e,
##para testarem seus conhecimentos sobre OPERADORES, propõem o seguinte:

##Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:

#primeiro output: deve apresentar como resultado o dobro do valor inserido;
#segundo output: deve apresentar como resultado o triplo do valor inserido;
#terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
#quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
#quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.


#inserir um valor
#valor inserido *2
#valor inserido *3
#valor inserido * valor inserido
#valor inserido ** (1/2)
#valor inserido ** (1/3)

print("Digite seus numeros:")

n1 = float(input ("Digite seu numero:"))
print("Primeiro número", (n1*2) )

n2 = float(input ("Digite seu numero:"))
print("segundo número", (n2*3) )

n3 = float(input ("Digite seu numero:"))
print("terceiro numero", n3**(2))

n4 = float(input ("Digite seu numero:"))
print("Quarto numero", n4**(1/2))

n5 = float(input ("Digite seu numero:"))
print("Quinto número", n5**(1/3) )



