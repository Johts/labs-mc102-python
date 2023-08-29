import sys
sys.setrecursionlimit(32771)


def conex(pixel_atual: int, pixel_seed: int, toler: int) -> bool:
    """Define uma tolerância para o pixel"""
    return abs(pixel_atual - pixel_seed) <= toler


def posicao(pos: int, dimensao_max: int):
    """Define se uma posição adjacente pode ser escolhida ou não"""
    if pos <= 0:
        return 0
    elif pos >= dimensao_max:
        return dimensao_max - 1
    else:
        return pos


def bucket(arquivo: list, intensidade: int, limiar: int,
           col: int, row: int, cor_seed: int):
    """Ferramenta balde, que preenche todos os pixels na região de tolerância
    com a intensidade desejada"""
    pixel = (row, col)
    max_dim = (len(arquivo), len(arquivo[0]))
    pixel_adj = [
        (row, posicao(col - 1, max_dim[1])),  # Cima
        (row, posicao(col + 1, max_dim[1])),  # Baixo
        (posicao(row - 1, max_dim[0]), col),  # Esquerda
        (posicao(row + 1, max_dim[0]), col),  # Direita
        (posicao(row + 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Dir.
        (posicao(row + 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Dir.
        (posicao(row - 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Esq.
        (posicao(row - 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Esq.
    ]
    arquivo[pixel[0]][pixel[1]] = intensidade
    for i in pixel_adj:
        if (conex(cor_seed, arquivo[i[0]][i[1]], limiar)
           and arquivo[i[0]][i[1]] != intensidade
           and i != pixel):
            bucket(arquivo, intensidade, limiar, i[1], i[0], cor_seed)


def negative(arquivo: list, limiar: int, col: int, row: int,
             max_intens: int, cor_seed: int):
    """Função negativa, que inverte a cor de todos os pixels adjacentes dentro
    do limiar de tolerância"""
    pixel = (row, col)
    max_dim = (len(arquivo), len(arquivo[0]))
    pixel_adj = [
        (row, posicao(col - 1, max_dim[1])),  # Cima
        (row, posicao(col + 1, max_dim[1])),  # Baixo
        (posicao(row - 1, max_dim[0]), col),  # Esquerda
        (posicao(row + 1, max_dim[0]), col),  # Direita
        (posicao(row + 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Dir.
        (posicao(row + 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Dir.
        (posicao(row - 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Esq.
        (posicao(row - 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Esq.
    ]
    arquivo[pixel[0]][pixel[1]] = max_intens - arquivo[pixel[0]][pixel[1]]
    for i in pixel_adj:
        if conex(cor_seed, arquivo[i[0]][i[1]], limiar) and i != pixel:
            negative(arquivo, limiar, i[1], i[0], max_intens, cor_seed)


def cmask(arquivo: list, limiar: int, col: int, row: int,
          cor_seed: int, arquivo_mask: list):
    """Função máscara complementar, que define todos os pixels dentro do limiar
    com intensidade 0 e o resto com intensidade 255"""
    pixel = (row, col)
    max_dim = (len(arquivo), len(arquivo[0]))
    pixel_adj = [
        (row, posicao(col - 1, max_dim[1])),  # Cima
        (row, posicao(col + 1, max_dim[1])),  # Baixo
        (posicao(row - 1, max_dim[0]), col),  # Esquerda
        (posicao(row + 1, max_dim[0]), col),  # Direita
        (posicao(row + 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Dir.
        (posicao(row + 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Dir.
        (posicao(row - 1, max_dim[0]), posicao(col - 1, max_dim[1])),  # Dg. Inf. Esq.
        (posicao(row - 1, max_dim[0]), posicao(col + 1, max_dim[1])),  # Dg. Sup. Esq.
    ]
    arquivo_mask[pixel[0]][pixel[1]] = 0
    for i in pixel_adj:
        if (conex(cor_seed, arquivo[i[0]][i[1]], limiar) and i != pixel
           and arquivo_mask[i[0]][i[1]] != 0):
            cmask(arquivo, limiar, i[1], i[0], cor_seed, arquivo_mask)


def save(arquivo: list, intensidade_max: int):
    """Salva e printa a imagem criada"""
    print("P2")
    print("# Imagem criada pelo lab13")
    print(f"{len(arquivo[0])} {len(arquivo)}")
    print(intensidade_max)
    for i in arquivo:
        print(" ".join([str(j) for j in i]))


# Abre o arquivo e transforma as informações necessárias em ints
arquivo = open(input()).read()
arquivo = arquivo.split("\n")[2:-1]
for i in range(len(arquivo)):
    lista_aux = arquivo[i].split()
    for j in range(len(lista_aux)):
        lista_aux[j] = int(lista_aux[j])
    arquivo[i] = lista_aux

# Define as variáveis necessárias
dimensoes = tuple(i for i in arquivo[0])
max_intens = arquivo[1][0]
arquivo = arquivo[2:]

n_de_comandos = int(input())
for i in range(n_de_comandos):
    comando = input().split()
    if comando[0] == "save":
        save(arquivo, max_intens)
    else:
        cor_seed = arquivo[int(comando[-1])][int(comando[-2])]
        if comando[0] == "bucket":
            bucket(arquivo, int(comando[1]), int(comando[2]),
                   int(comando[3]), int(comando[4]), cor_seed)
        elif comando[0] == "negative":
            negative(arquivo, int(comando[1]), int(comando[2]),
                     int(comando[3]), max_intens, cor_seed)
        elif comando[0] == "cmask":
            arquivo_mask = [[255 for j in range(dimensoes[0])]
                            for i in range(dimensoes[1])]
            cmask(arquivo, int(comando[1]), int(comando[2]),
                  int(comando[3]), cor_seed, arquivo_mask)
            arquivo = arquivo_mask
