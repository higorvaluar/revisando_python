"""
Valores padrão para parâmetros:

Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão
será usado.

Refatorar = editar o seu código.
"""
# 0 é considero FALSE em condições

def soma(x, y, z = None):
    if z is not None:
        print(f'{x = } {y =} {z =}', x + y + z)
    else:
        print(f'{x =} {y = }', x + y)

soma(1, 2, 0)
soma(3, 5)
soma(100, 2323)
soma(y = 9, z = 0, x = 1)