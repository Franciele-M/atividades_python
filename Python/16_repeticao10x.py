'''Titulo: Print 10 vezes
Autor: Franciele
Data: 01/10/2024
Descrição: Faça um programa que leia uma palavra qualquer e a imprima 10 vezes '''

#entrada de dados
palavra = input("Escreva uma palavra: ")
contador = 1

#processamento de dados e saída

while contador < 11:
    print(f'{palavra} --- repetiu {contador} vezes')
    contador = contador + 1
