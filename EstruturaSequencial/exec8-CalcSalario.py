#Exercício 8:
#Faça um programa que pergunte o quanto você ganha por hora e o número de horas trabalhadas no mês
#Calcule e mostre o total do seu salário no referido mês

print(" --------------------------------------------------")
print("|Saiba o quanto receberá de salário no fim do mês: |")
print(" --------------------------------------------------")
valor_hora = float(input("Quanto você recebe por hora trabalhada ? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas no mês ? "))
salario = valor_hora * horas_trabalhadas
print("\n Você terá um salário de: R$", salario)