def sign(x: int) -> int:
    """Retorna o sinal de x"""
 
    if x == 0:
        return 0
    else:
        return int(abs(x)/x)
 
 
def move_robot(r_posf: list, room: list, turn_back: bool) -> list:
    """Move o robô no modo escaneamento e retorna sua posição"""
 
    # A variável turn_back decide se o robô deve voltar para o canto inf. dir.
 
    if r_posf[0] % 2 == 0 and r_posf[1] < len(room[0]) - 1:
        r_posf[1] += 1
    elif r_posf[0] % 2 == 0 and r_posf[1] == len(room[0]) - 1:
        if r_posf[0] < len(room) - 1:
            r_posf[0] += 1
    elif r_posf[0] % 2 == 1 and r_posf[1] > 0:
        if turn_back:
            r_posf[1] += 1
        else:
            r_posf[1] -= 1
    elif r_posf[0] % 2 == 1 and r_posf[1] == 0:
        if r_posf[0] < len(room) - 1:
            r_posf[0] += 1
        elif turn_back:
            r_posf[1] += 1
 
    return r_posf
 
 
def end(r_posf: list, room: list) -> bool:
    """Checa se o robô está no final da sala ou não"""
 
    if r_posf[1] == len(room[0]) - 1 and r_posf[0] == len(room) - 1:
        return False
    else:
        return True
 
 
# Define a sala inicial
n_de_linhas = int(input())
sala = []
for i in range(n_de_linhas):
    linha_lista = input().split()
    sala.append(linha_lista)
 
# Lista que recebe a posição do robô:
r_pos = [0, 0]
 
running = True
 
# Printa o estado inicial da sala
for i in range(len(sala)):
    string = " ".join(sala[i])
    print(string)
print()
 
escaneamento_bool = True
n = 0 
n2 = 0 
while running:
    sala[r_pos[0]][r_pos[1]] = "."
 
    sala_adjacente = [
        [r_pos[0], r_pos[1] - 1 if r_pos[1] - 1 >= 0 else r_pos[1]],  # Esquerda
        [r_pos[0] - 1 if r_pos[0] - 1 >= 0 else r_pos[0], r_pos[1]],  # Cima
        [r_pos[0], r_pos[1] + 1 if r_pos[1] + 1 <= len(sala[0]) - 1 else r_pos[1]],  # Direita
        [r_pos[0] + 1 if r_pos[0] + 1 <= len(sala) - 1 else r_pos[0], r_pos[1]]  # Baixo
    ]
 
    # Checa se há sujeiras nos quadrados adjacentes
    lista_bool = [sala[i[0]][i[1]] == "o" for i in sala_adjacente]
 
    if any(lista_bool):
        not_clean = False
        if n == 0:
            # Guarda a posição antes de entrar na limpeza
            escan_posit = list(r_pos)
 
        # Muda a posição do robô para a sujeira
        r_pos = sala_adjacente[lista_bool.index(True)]
        if move_robot(list(escan_posit), sala, n2) == r_pos:
            # Se a sujeira estava no caminho do escaneamento
 
            escan_posit = list(r_pos)
            escaneamento_bool = True
        else:
            escaneamento_bool = False
        n += 1
    elif escaneamento_bool is False:
        """Entra aqui se uma sujeira foi limpada antes mas fora do caminho
        E se não há mais sujeira nas posições adjacentes """
 
        # Determina se vai para esquerda/direita/cima/baixo depois da limpeza
        x_sign = sign(r_pos[1] - escan_posit[1])
        y_sign = sign(r_pos[0] - escan_posit[0])
 
        if r_pos[1] != escan_posit[1]:
            r_pos[1] -= x_sign
        elif r_pos[0] != escan_posit[0]:
            r_pos[0] -= y_sign
        else:
            # Entra no modo escaneamento se nenhuma sujeira for achada
            escaneamento_bool = True
            r_pos = move_robot(r_pos, sala, n2)
            n = 0
    else:
        # Entra no modo escaneamento se nenhuma sujeiro for achada
        escaneamento_bool = True
        not_clean = True
        r_pos = move_robot(r_pos, sala, n2)
        n = 0
 
    sala[r_pos[0]][r_pos[1]] = "r"
 
    if r_pos[1] == 0 and r_pos[0] == len(sala) - 1 and r_pos[0] % 2 == 1:
        n2 = True
 
    if r_pos[1] == len(sala[0]) - 1 and r_pos[0] == len(sala) - 1 and r_pos[0] % 2 == 1:
        if n2 and not_clean:
            running = end(r_pos, sala)
    elif not_clean:
        running = end(r_pos, sala)
 
    # Printa como está a sala depois do robô se mover
    for i in range(len(sala)):
        string = " ".join(sala[i])
        print(string)
 
    if running:
        print()
 
