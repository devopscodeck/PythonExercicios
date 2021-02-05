#Exercício 14:    obs( Os exercícios 13 e 12 estão duplicados, na lista oficial)
#João deve pagar multa de R$4,00 por kg execedente a partir dos 50kg permitidos
#Calcule a multa que João deverá pagar por kg em excesso
#A titulo de simplificação iremos considerar apenas os valores inteiros

quantidade_peixes = int(input("Digite a quantidade em kg de peixe registrada na balança: "))
calcula_multa = (quantidade_peixes - 50 ) * 4.00

print("O valor da multa excedente será de R$ ", calcula_multa)