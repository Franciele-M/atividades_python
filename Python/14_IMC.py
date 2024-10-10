'''Titulo: Qual o seu IMC?
Autor: Franciele
Data: 26/09/2024
Descrição: Escreva um algoritmo que a partir da massa e da altura informados pelo usuário, 
calcule e apresente seu IMC e sua classificação '''


#entrada de dados

imc = float(input("Informe o seu IMC: "))

#processamento de dados e saída

if imc < 18:
    print("Magreza")

elif imc >= 18 and imc <= 24.9:
    print("Saudável")

elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")

elif imc >= 30:
    print("Obesidade")


