"""
Argumentos nomeados e não nomeados em funções Python:

1. Argumento nomeado tem nome com sinal de igual.
2. Argumento não nomeado recebe apenas o argumento (valor).
"""

def soma(x, y, z):
    # Definição
    print(f'{x = }, y = {y}, z = {z}', '|', 'x + y + z=', x + y + z)

soma(1, 5, 3)
soma(4, 9, 4)
soma(y = 4, x = 3, z = 6)
soma(1, 2, z = 9)

print(1, 4, 9, sep = '-')