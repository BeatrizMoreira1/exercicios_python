
soma_notas = 0

for i in range(5):
    
    nota = float(input(f"Digite a nota {i + 1}: "))
    
    soma_notas += nota

media = soma_notas / 5

print(f"A média das notas é: {media:.2f}")

Pedieu pedi ao usuário para inserir 5 notas.
Somar todas essas notas.
Dividir a soma por 5.
Exibir o resultado final formatado.