'''Titulo: Apresentar números impares
Autor: Franciele
Data: 01/10/2024
Descrição: Faça um programa que receba dois valores, sendo que o primeiro 
deve ser menor que o segundo. O programa deve apresentar todos os 
números ímpares contidos nesta sequência. 
(Modulo %. Exemplo: 7%2 = 1~. Entre 10 e 20, print apenas números impares: 11, 13, 15...) '''


#entrada de dados

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))


#Processamento e saída de dados
num = a
while num <= b:
    if num % 2 != 0:
        print(num)
    num += 1
    