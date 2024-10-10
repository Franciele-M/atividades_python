'''Titulo: Faixa Etária
Autor: Franciele
Data: 26/09/2024
Descrição: Faça um programa que receba a idade do indivíduo e informe a sua faixa etária '''



#entrada de dados

idade = int(input("Informe a sua idade: "))


#processamento de dados e saída

if idade <= 12:
    print("Você é uma criança")

elif idade >= 13 and idade <= 17:
    print("Você é um adolescente")

elif idade >= 18 and idade <= 59:
    print("Você é um adulto")

elif idade >= 60:
    print("Você é um especialista")






