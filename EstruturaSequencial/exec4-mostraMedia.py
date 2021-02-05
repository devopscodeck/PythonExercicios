#Exercício 4
#Faça um programa que peça as 4 notas bimestrais e mostre a média


primeiro_bimestre = int(input("Digite a primeira nota do bimestre: "))
segundo_bimestre  = int(input("Digite a segunda nota do bimestre: "))
terceiro_bimestre = int(input("Digite a terceira nota do bimestre: "))
quarto_bimestre   = int(input("Digite a quarta nota do bimestre: "))
media_bimestral   = int((primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4)

print("A média bimestral é: ",media_bimestral)