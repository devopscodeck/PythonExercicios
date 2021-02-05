#Exercício 11:
#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo
# b) a soma do triplo do primeiro com o terceiro
# c) o terceiro elevado ao cubo

primeiro_numero_inteiro = int(input("Digite um número inteiro: "))
segundo_numero_inteiro  = int(input("Digite o segundo número inteiro: "))
numero_real             = float(input("Digite um número real: "))

produto_primero_com_metade_do_segundo = primeiro_numero_inteiro + (segundo_numero_inteiro / 2 )
soma_triplo_do_primeiro_com_terceiro  = (primeiro_numero_inteiro * 3) + numero_real
terceiro_elevado_ao_cubo              = numero_real ** 3

print("\nO produto do dobro do primeiro número com metade do segundo é: ", produto_primero_com_metade_do_segundo)
print("\nA soma do triplo do primeiro com o terceiro: ", soma_triplo_do_primeiro_com_terceiro)
print("\nO terceiro elevado ao cubo: ", terceiro_elevado_ao_cubo)

