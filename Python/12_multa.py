'''Titulo: Tabela de Multas?
Autor: Franciele
Data: 26/09/2024
Descrição: Escreva um programa que leia a velocidade máxima permitida em uma avenida e 
velocidade com que o motorista estava dirigindo nela e calcule a multa que uma 
pessoa vai receber '''


#entrada de dados

velocidade = int(input("Informe a sua velocidade: "))

#processamento de dados e saída

if velocidade == 10:
    print("Você estava a 10km/h. Sua multa será de R$50,00")

elif velocidade >= 11 and velocidade <= 30:
    print("Você estava acima de 10 km/h. Sua multa será de R$100,00")

elif velocidade >= 31:
    print("Você estava acima de 30km/h. Sua multa será de R$200,00")

else:
    print("Tranquilo. Não há multas.")

