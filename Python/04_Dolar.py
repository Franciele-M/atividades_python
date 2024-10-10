'''Titulo: Dolar
Autor: Franciele
Data: 19/09/2024
Descrição: Desenvolver um algoritmo que um valor da moeda real, 
a cotação da conversão real para dolar, e apresente a
quantidade desse valor em dolar. '''


#entrada de dados
real = int(input("Informe o valor do Real: "))
dolar = int(input("Insira o valor da cotação: "))

#processamento de dados
resultado = real / dolar

#Saída de dados
print("R$" + str(float(real)) + " equivale a $" + str(float(resultado)))

#print(f'R$ {real} equivale ${dolar}') F = formatar

