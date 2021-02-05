#Exercicio 7
#Faça um programa que calcule a área de um quadrado, e em seguida mostre o *dobro* desta área para o usuário

base = float(input("Digite o valor da base do quadrado: "))

#Por ser um quadrado, base e altura possuem o mesmo tamanho, logo a base ao quadrado resolve nosso problema

dobro_area_quadrado = (base ** 2) * 2
print("O dobro da área do quadrado será: ", dobro_area_quadrado)