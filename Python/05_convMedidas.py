'''Titulo: Conversão de Unidades
Autor: Franciele
Data: 24/09/2024
Descrição: Desenvolver um algoritmo que receba o número de pés, faça as conversões
a seguir e mostre os resultados:
- Polegadas;
- Jardas;
- Milhas
Sabendo que: 
- 1 pé = 12 polegadas;
- 1 jarda = 3 pés;
- 1 milha = 1.760 jardas. '''

#entrada de dados

#ctrl + ; = comentário

pe = int(input("Informe o número de Pés: "))


#processamento de dados

polegadas = pe * 12
jardas = pe / 3 
milhas = (pe / 3) / 1760

#Saída de dados


print(f"{pe} pé(s) = {jardas} jardas") 
print(f"{pe} pé(s) = {polegadas} polegadas") 
print(f"{pe} pé(s) = {milhas} milhas") 


