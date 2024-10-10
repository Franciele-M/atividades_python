'''Titulo: Tabuada
Autor: Franciele
Data: 01/10/2024
Descrição: Faça um programa que calcule a tabuada de um número digitado pelo usuário '''

#entrada de dados
x = int(input('Informe um número de 1 a 10 para saber a tabuada da multiplicação '))

y = 0 #números aleatórios
r = 0 #resultado

#processamento de dados
while y < 10:
    y = y + 1
    r = x * y

 
# Saida de dados   
    print( x, '*', y, '=', r )

