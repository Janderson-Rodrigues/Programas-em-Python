def mover_disco(origem, destino):
    disco = origem.pop()
    destino.append(disco)

def imprimir_torres(torre_A, torre_B, torre_C):
    print('A:', torre_A)
    print('B:', torre_B)
    print('C:', torre_C)
    print()

# Logica da função recursiva.

def torres_de_hanoi_recursivo(num_dsico, origem, destino, auxiliar):
    if num_dsico == 1:
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
    else:
        torres_de_hanoi_recursivo(num_dsico -1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_dsico - 1, auxiliar, destino, origem)

# Resolvendo o problema recursivamente
num_disco = 7
# Inicializando as torres e os discos 
torre_A = list(range(num_disco, 0, -1))
torre_B = []
torre_C = []
# mostrando o estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo(num_disco, torre_A, torre_C, torre_B)