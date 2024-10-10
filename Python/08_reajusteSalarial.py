'''Titulo: Reajuste do Salario (atividade 6)
Autor: Franciele
Data: 26/09/2024
Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo 
salário, sabendo-se que:
Salário < R$ 1000,00 aumento de 25%.
Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
Salário >= R$ 2000,00 aumento de 10% '''


#entrada de dados

salario = int(input("Informe seu salário: R$"))

#processamento de dados e saída

if salario < 1000 and salario > 0:
    salario_atual = salario + (salario * 0.25)
    print(f"Ocorreu um reajuste de 25%. O Salário atual é R${salario_atual}")


elif salario >= 1000 and salario < 2000:
    salario_atual = salario + (salario * 0.15)
    print(f"Ocorreu um reajuste de 15%. O Salário atual é R${salario_atual}")


elif salario >= 2000:
    salario_atual = salario + (salario * 0.10)
    print(f"Ocorreu um reajuste de 10%. O Salário atual é R${salario_atual}")


else:
    print("Ocorreu um erro")



