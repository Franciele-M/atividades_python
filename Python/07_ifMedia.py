'''Titulo: Média Aritmética das Notas (estudo 'if')
Autor: Franciele
Data: 26/09/2024
Descrição: Faça um programa que receba 4 notas e informe a média aritmética e se o aluno foi aprovado, reprovado ou está de 
recuperação. '''




#entrada de dados

nota1 = int(input("Informe a primeira nota:  "))
nota2 = int(input("Informe a segunda nota:  "))
nota3 = int(input("Informe a terceira nota:  "))
nota4 = int(input("Informe a quarta nota:  "))

#processamento de dados e 

media = (nota1 + nota2 + nota3 + nota4)/4


# saída

if media >= 6:
    print(f"A média é {media}, você está APROVADO!")

elif media >= 4:
    print(f"A média é {media}, você está de RECUPERAÇÃO!")

else:
    print(f"A média é {media}, você está REPROVADO!")


