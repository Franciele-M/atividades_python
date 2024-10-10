'''Titulo: Qual a sua profissão?
Autor: Franciele
Data: 26/09/2024
Descrição: Faça um programa que informe a sua ocupação a partir do seu código de profissão '''


#entrada de dados

codigo = int(input("Informe o seu código de profissão (1 à 5): "))


#processamento de dados e saída

if codigo == 1:
    print("Você é um matemático")

elif codigo == 2:
    print("Você é um analista de sistemas")

elif codigo == 3:
    print("Você é um físico")

elif codigo == 4:
    print("Você é um arquiteto")

elif codigo == 5:
    print("Você é um piloto de aeronaves")

else:
    print("Você é um desempregado")






