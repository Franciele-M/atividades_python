"""
Titulo: Média dos 6 alunos
Autor: Franciele
Data: 08/10/2024
Descrição: Faça um programa que receba duas notas de seis alunos. 
Calcule e mostre: 
- A média aritmética das duas notas de cada aluno; e
- A mensagem que está na tabela a seguir:
| Média Aritmética | Mensagem |
| Até 3            | Reprovado|
| Entre 3 e 7      |   Exame  |
| De 7 para cima   | Aprovado |
- O total de alunos aprovados; 
- O total de alunos de exame; 
- O total de alunos reprovados; 
- A média da classe.
"""

# "\n" = quebra de linhas
# range = gera uma sequência
#ex.: n = range(10)   print(n)  = print(0, 9) (print: início e fim, apenas 2 digítos)
#ex.2: n = range(10)   print(list(n))  = print(0,1,2...7,8,9)



# Entrada de dados
total_alunos = 6
aprovados = 0
exame = 0
reprovados = 0
soma_das_medias = 0

# Processamento de dados
# Loop para receber as notas de cada aluno
for i in range(total_alunos):
    print(f"\nAluno {i + 1}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Calculando a média
    media = (nota1 + nota2) / 2
    soma_das_medias += media
    
    # Determinando a mensagem com base na média
    if media <= 3:
        print("Média:", media, "- Mensagem: Reprovado")
        reprovados += 1
    elif 3 < media < 7:
        print("Média:", media, "- Mensagem: Exame")
        exame += 1
    else:
        print("Média:", media, "- Mensagem: Aprovado")
        aprovados += 1

# Cálculo da média da classe
media_classe = soma_das_medias / total_alunos

# Saída de dados
# Exibindo os resultados finais
print("\nTotal de alunos aprovados:", aprovados)
print("Total de alunos de exame:", exame)
print("Total de alunos reprovados:", reprovados)
print("Média da classe:", media_classe)







