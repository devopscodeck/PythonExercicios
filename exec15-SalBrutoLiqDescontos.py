#Exercício 15:
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:


print(" --------------------------------------------------")
print("|Saiba o quanto receberá de salário no fim do mês com os descontos: |")
print(" --------------------------------------------------")
valor_hora = float(input("Quanto você recebe por hora trabalhada ? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas no mês ? "))
salario_bruto = valor_hora * horas_trabalhadas

print("\nVocê terá um salário bruto de: R$", salario_bruto)
desconto_inss      = salario_bruto * (8/100)
desconto_IR        = salario_bruto * (11/100)
desconto_sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - (desconto_sindicato + desconto_IR + desconto_inss)

print("você pagou ao INSS: R$", desconto_inss)
print("você pagou de IR: R$", desconto_IR)
print("você pagou ao Sindicato: R$", desconto_sindicato)
print("Seu salário líquido é de: R$", salario_liquido)

