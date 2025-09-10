
X = int(input())       # Distância total percorrida (em Km)
Y = float(input())     # Combustível gasto (em litros)

# Cálculo do consumo médio
consumo = X / Y

# Impressão do resultado com 3 casasimais
print(f"{consumo:.3f} km/l")
