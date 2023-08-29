def dano(dano_max: int, c: tuple, f: tuple) -> int:
    """Calcula o dano em relação ao ponto crítico"""

    d = dano_max - abs(c[0] - f[0]) - abs(c[1] - f[1])
    if d >= 0:
        return d
    else:
        return 0


def cura(vida: int, vida_max: int) -> int:
    """Cura a Aloy depois de cada rodada"""

    if vida + vida_max // 2 <= vida_max:
        return vida + vida_max // 2
    else:
        return vida_max


def converte_int(lista: list) -> list:
    """Converte todos os elementos numéricos de uma lista em ints"""

    for i in range(len(lista)):
        # O "[1:]" desconsidera o sinal do número
        if lista[i][1:].isnumeric() or lista[i].isnumeric():
            lista[i] = int(lista[i])

    return lista


def consegue_flechas() -> dict:
    """Consegue um dicionário de flechas com o input do usuário"""

    flechas_input = input().split()
    # Cria um dicionário {tipo_de_flecha: quantidade}
    flechas_dict = {}

    for i in range(len(flechas_input)//2):
        flechas_dict[flechas_input[2 * i]] = int(flechas_input[2 * i + 1])

    return flechas_dict


def consegue_maquina(n_de_maquinas: int) -> list:
    """Consegue as máquinas que serão enfrentadas"""

    lista_maquina = []
    # Cada elemento da lista será uma lista com uma máquina
    # Cada máquina será da forma:
    # [vida, dano, partes_dict]
    for i in range(n_de_maquinas):
        lista_maquina.append(input().split())
        partes_dict = {}

        for _ in range(int(lista_maquina[i][2])):
            # Cada máquina terá um dicionário em maquina[3] com suas partes

            # Lista temporária [parte, fraqueza, dano_max, cx, cy]
            lista_partes = input().split(", ")

            # Dicionário = {parte: [fraqueza, dano, (cx, cy)]}
            partes_dict[lista_partes[0]] = [
                lista_partes[1], int(lista_partes[2]),
                (int(lista_partes[3]), int(lista_partes[4]))
            ]

        lista_maquina[i] = converte_int(lista_maquina[i])
        lista_maquina[i][2] = partes_dict

    return lista_maquina


def consegue_comando() -> list:
    """Consegue o comando do usuário em forma de lista"""

    command = input().split(", ")
    # Transforma os números em ints
    command = converte_int(command)
    # Coordenadas da flecha em tupla
    command[3] = (command[3], command[4])
    command.pop(4)

    return command


def fraqueza_checker(tipo_da_flecha: str, fraqueza_do_corpo: str) -> bool:
    """Checa se o tipo da flecha é compatível com a fraqueza"""

    if fraqueza_do_corpo == "todas":
        return True
    elif fraqueza_do_corpo == "nenhuma":
        return False
    else:
        if tipo_da_flecha == fraqueza_do_corpo:
            return True
        else:
            return False


def causa_dano(command: list, machine: list) -> list:
    """Retorna o dano causado pela Aloy à máquina"""

    if fraqueza_checker(command[2], machine[command[0]][2][command[1]][0]):
        # Se a flecha for do mesmo tipo da fraqueza:
        machine[command[0]][0] -= dano(
            machine[command[0]][2][command[1]][1],
            machine[command[0]][2][command[1]][2],
            command[3]
        )
    else:
        machine[command[0]][0] -= dano(
            machine[command[0]][2][command[1]][1],
            machine[command[0]][2][command[1]][2],
            command[3]
        ) // 2

    if machine[command[0]][0] <= 0:
        machine[command[0]][0] = 0

    return machine


def consegue_criticos(command: list, machine: list, critic_dict: dict) -> dict:
    """Dicionário de críticos com a posição, a máquina e a quantidade"""

    if machine[command[0]][2][command[1]][2] == command[3]:
        if command[3] not in list(critic_dict[command[0]].keys()):
            critic_dict[command[0]][command[3]] = 1
        else:
            critic_dict[command[0]][command[3]] += 1
"""        if command[3] in critic_dict[command[0]]:
            critic_dict[command[0]][1] += 1
        elif critic_dict[command[0]] == []:
            critic_dict[command[0]] = [command[3], 1]
        else:
            critic_dict[command[0]].append()"""


def main() -> None:
    """Função principal do código"""

    # Consegue os dados do usuário
    vida = vida_max = int(input())
    flechas = consegue_flechas()
    flechas_copia = dict(flechas)
    n_monstros = int(input())
    nao_morto = True
    n_de_combate = 0

    while n_monstros > 0 and nao_morto:
        # Roda enquanto estiver monstros vivos ou a Aloy não estar morta

        n_maquinas = int(input())
        lista_maquina = consegue_maquina(n_maquinas)
        flechas = dict(flechas_copia)

        vida_monstros_total = 0
        flechas_total = 0
        flechas_utilizadas = {i: 0 for i in list(flechas.keys())}
        dicionario_criticos = {i: {} for i in range(n_maquinas)}

        for i in flechas:
            flechas_total += flechas[i]
        for i in lista_maquina:
            vida_monstros_total += i[0]
        print(f"Combate {n_de_combate}, vida = {vida}")
        while vida_monstros_total > 0:
            for i in range(3):
                comando = consegue_comando()
                lista_maquina = causa_dano(comando, lista_maquina)
                flechas[comando[2]] -= 1
                flechas_total -= 1
                flechas_utilizadas[comando[2]] += 1
                vida_monstros_total = 0
                for i in lista_maquina:
                    vida_monstros_total += i[0]
                consegue_criticos(comando, lista_maquina, dicionario_criticos)
                # Checa se a máquina foi derrotada
                if lista_maquina[comando[0]][0] <= 0:
                    print(f"Máquina {comando[0]} derrotada")
                if vida_monstros_total <= 0 or flechas_total <= 0:
                    break

            for i in lista_maquina:
                if i[0] != 0:
                    vida -= i[1]

            # Checa se a Aloy morreu
            if vida <= 0:
                nao_morto = False
                vida = 0
                string_final = "Aloy foi derrotada em combate e não retornará a tribo."
                break

            # Checa se a Aloy está sem flechas
            if flechas_total <= 0:
                nao_morto = False
                string_final = "Aloy ficou sem flechas e recomeçará sua missão mais preparada."
                break

        n_de_combate += 1
        print(f"Vida após o combate = {vida}")
        if nao_morto:
            print("Flechas utilizadas:")
            for j in flechas_utilizadas:
                if flechas_utilizadas[j] != 0:
                    print(f"- {j}: {flechas_utilizadas[j]}/{flechas_copia[j]}")

        vida = cura(vida, vida_max)
        # Checa se houve críticos e imprime eles
        crit_bool = [dicionario_criticos[i] != {} for i in dicionario_criticos]
        if any(crit_bool):
            print("Críticos acertados:")
            for i in range(len(dicionario_criticos)):
                if dicionario_criticos[i] != {}:
                    coord_list = list(dicionario_criticos[i].keys())
                    print(f"Máquina {i}:")
                    for j in coord_list:
                        print(f"- {j}: {dicionario_criticos[i][j]}x")
        n_monstros -= n_maquinas

    if nao_morto:
        string_final = "Aloy provou seu valor e voltou para sua tribo."
    print(string_final)


main()
