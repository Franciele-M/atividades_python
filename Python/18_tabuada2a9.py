'''Titulo: Tabuada 2 a 9
Autor: Franciele
Data: 01/10/2024
Descrição: Faça um programa que calcula a tabuada dos números 2 a 9 '''

#entrada de dados
x = int(input('Informe um número de 1 a 10 para saber a tabuada da multiplicação '))

y = 1 #números aleatórios
r = 0 #resultado

#processamento de dados
while y < 9:
    y = y + 1
    r = x * y


# Saida de dados   
    print( x, '*', y, '=', r )

