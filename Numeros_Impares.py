# Escreva e demonstre (lógica / código / compilação / execução) um programa que receba uma sequência de números inteiros e retorne apenas os números ímpares.

# ~ título ~
print("\n")
print("\t\t\tDETECTOR DE NÚMEROS ÍMPARES\n")

# estrutura de repetição para que o arquivo executável não se feche tão rapidamente
while True:
    # criamos uma lista, onde os números digitados serão armazenados 
    numeros = []

    # inicializamos o contador
    i = 1

    print("\n")

    # com outra estrutura while, fazemos com que o bloco de código se repita enquanto o contador for menor que 6, ou seja, 5 vezes
    while i < 6:
        try:
            x = int(input("Escreva um número inteiro: "))
            # toda vez que esse bloco roda, o contador soma 1
            i += 1
            
            # condição: se o resto da divisão do número entrado for igual a 1 (ou seja, se for ímpar), o número é adicionado à lista
            if x % 2 == 1:
                numeros.append(x)

        # try except para detectar erros na entrada do usuário
        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")

    # condição que verifica se o tamanho da lista é igual a 0, isto é, se estiver vazia
    if len(numeros) == 0:
        print("\nNão há números ímpares!\n")
    else:
        print("\nNúmeros ímpares digitados: ", numeros, "\n")

    op = input("Deseja jogar novamente? [S/N] ").upper()
    if op != 'S':
        print("Obrigada por jogar!\n")
        break