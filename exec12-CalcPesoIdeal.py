#Exercicio 12:
#Tendo como dado de dentrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
#as seguintes formulas:  a. Para homens: (72.7*h) -58    b. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite aqui a sua altura: "))
genero = input("Você é do sexo feminino ou masculino ? ").upper()

peso_ideal_masculino = (altura * 72.7) - 58
peso_ideal_feminino  = (altura * 62.1) - 44.7

if genero == "MASCULINO":
    print("Seu peso ideal é: ",peso_ideal_masculino)
elif genero == "FEMININO":
    print("Seu peso ideal é: ",peso_ideal_feminino)
else:
    print("Por favor, digite o sexo apenas feminino ou masculino: ")
