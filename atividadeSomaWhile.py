
soma = 0

print("Digite os números inteiros para somar.")
print("Quando quiser terminar, digite a palavra 'fim'")

while True:
    
    entrada = input("Digite um número: ")

    if entrada.lower() == 'fim':
         
        break

    try:
       
        numero = int(entrada)

        soma += numero
 
    except ValueError:
        
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print(f"\nA soma total dos números digitados é: {soma}")
#Este código foi feito para somar uma quantidade indefinida de números inteiros