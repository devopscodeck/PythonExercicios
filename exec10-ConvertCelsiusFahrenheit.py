#Exercício 10
#Faça um programa que peça a temperatura em graus Celsius , converta e mostre o resultado em Fahrenheit

graus_celsius = float(input("Entre com uma temperatura em C° "))
convert_for_fahrenheit = (graus_celsius / 5 ) * 9 + 32
print("A temperatura convertida para fahrenheit é de : ", convert_for_fahrenheit)

#C = 5 * (( F -32) / 9 )
#(C / 5) * 9 + 32 = F  < -- fórmula para descobrir a temperatura em fahrenheit