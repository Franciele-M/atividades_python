'''Titulo: Qual o seu Lanche?
Autor: Franciele
Data: 26/09/2024
Descrição: Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do 
mesmo pelo usuário '''


#entrada de dados

codigo = int(input("Informe o seu número do seu lanche (1 à 5): "))


#processamento de dados e saída

if codigo == 1:
    print("Saindo um Big Mac")

elif codigo == 2:
    print("Saindo um Quarteirão")

elif codigo == 3:
    print("Saindo um McChicken")

elif codigo == 4:
    print("Saindo um Cheddar McMelt")

elif codigo == 5:
    print("Saindo um McMax")

else:
    print("Saindo um Xnada!")
