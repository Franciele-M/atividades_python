'''Titulo: É um triângulo?
Autor: Franciele
Data: 26/09/2024
Descrição: Faça um programa que receba 3 valores e verifique se eles podem representar os 
lados em um triângulo '''


#entrada de dados

lados = int(input("Quantos lados iguais tem a figura?: "))

#processamento de dados e saída

if lados == 3:
    print("É um triângulo equilátero")

elif lados == 2:
    print("É um triângulo isósceles")

elif lados == 0:
    print("É um triângulo escaleno")

else:
    print("Não é um triângulo ")

