# Solicita ao usuário que insira um número inteiro
n = int(input("Digite um número inteiro: "))

# Utiliza um laço for para gerar a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
#é um tipo de dado que representa números inteiros, ou seja, números sem parte decimal, positivos ou negativos. É usado para armazenar valores numéricos inteiros e desempenha um papel fundamental
#for é uma estrutura de controle de fluxo usada para iterar sobre sequências (como listas, tuplas, strings, etc.) ou outros iteráveis