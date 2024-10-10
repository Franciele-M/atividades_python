'''Titulo: Salario
Autor: Franciele
Data: 24/09/2024
Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo 
salário, sabendo-se que este sofreu um aumento de 25%. '''


#entrada de dados

salario = int(input("Informe seu salário: "))


#processamento de dados

reajuste = salario + (salario * 0.25)


#Saída de dados

print(f"O seu novo salário é: R${reajuste}")
