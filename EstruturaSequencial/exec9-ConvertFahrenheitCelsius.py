#Exercício 9:
#Faça um programa que peça a temperatura em Fahrenheit e realize a conversão para Graus Celsius.


graus_fahrenheit = float(input("Digite aqui a temperaturo em Fahrenheit: "))
graus_celsius = 5 * ((graus_fahrenheit - 32) / 9)
print("A temperatura em Celsiu é de: ", graus_celsius, "C°")