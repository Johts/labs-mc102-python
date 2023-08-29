class Cartas:
    def __init__(self, carta: str):
        self._num_forca = {
            "A": 0, "2": 1, "3": 2,
            "4": 3, "5": 4, "6": 5,
            "7": 6, "8": 7, "9": 8,
            "10": 9, "J": 10, "Q": 11,
            "K": 12
        }
        self._naipe_forca = {
            "O": 0,
            "E": 1,
            "C": 2,
            "P": 3
        }

        self._naipe = carta[-1]
        self._numero = carta[:-1]
        self._naipe_value = self._naipe_forca[carta[-1]]
        self._numero_value = self._num_forca[carta[:-1]]

    @property
    def numero(self):
        return self._numero

    @property
    def naipe_value(self):
        return self._naipe_value

    @property
    def numero_value(self):
        return self._numero_value

    @property
    def tipo_carta(self):
        return self._numero + self._naipe

    def __gt__(self, other):
        """Define se uma carta é maior que outra"""
        if self.numero_value > other.numero_value:
            return True
        elif self.numero_value == other.numero_value:
            if self.naipe_value > other.naipe_value:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return ((self.numero_value == other.naipe_value) and
                (self.naipe_value == other.naipe_value))

    def __lt__(self, other):
        return not (self == other and self > other)

    def __ge__(self, other):
        return not (self < other)

    def __le__(self, other):
        return not (self > other)


class Jogador:
    def __init__(self, mao: list):
        self._mao = [Cartas(i) for i in mao]

    @property
    def mao(self):
        ordena(self._mao)
        return self._mao

    @mao.setter
    def mao(self, mao: list):
        ordena(mao)
        self._mao = mao

    def remove_carta(self, carta: Cartas):
        mao_nova = []
        for i in self.mao:
            if i.tipo_carta != carta.tipo_carta:
                mao_nova.append(i)
        self.mao = mao_nova

    def discarta(self, pilha: list, carta_força: Cartas):
        n = 0
        pilha_temporaria = []
        if any([i.numero_value == carta_força.numero_value for i in self.mao]):
            # Se existir cartas com o mesmo número da carta força
            index = busca(
                [i.numero_value for i in self.mao], carta_força.numero_value
                )

            if index == 0:
                # Evita que a lista fique vazia quando o index for 0
                lista_aux = self.mao.copy()[::-1]
            else:
                lista_aux = self.mao.copy()[:index - 1:-1]

            for i in lista_aux:
                if i.numero_value == carta_força.numero_value:
                    n += 1
                    pilha_temporaria.append(i)
        elif any([i.numero_value > carta_força.numero_value for i in self.mao]):
            # Se existir cartas maiores que a carta força
            for index in range(len(self.mao) - 1, - 1, -1):
                if self.mao[index].numero_value > carta_força.numero_value:
                    carta_aux = self.mao[index]
                    break
            lista_aux = self.mao.copy()[::-1]
            for i in lista_aux:
                if i.numero_value == carta_aux.numero_value:
                    n += 1
                    pilha_temporaria.append(i)
        else:
            lista_aux = self.mao.copy()[::-1]
            carta_aux = lista_aux[0]
            for i in lista_aux:
                if i.numero_value == carta_aux.numero_value:
                    n += 1
                    pilha_temporaria.append(i)
        """ for i in pilha_temporaria:
            print(i.tipo_carta, end=" ")
        print("PIlha temporária")"""
        for carta in pilha_temporaria:
            self.remove_carta(carta)
            pilha.append(carta)
        print(f"{n} carta(s) ", end="")


def ordena(lista: list):
    """Ordena uma lista usando selection sort"""
    for i in range(len(lista) - 1):
        maior = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[maior]:
                maior = j
        lista[i], lista[maior] = lista[maior], lista[i]


def busca(lista: list, item) -> int:
    """Busca um item em uma lista ordenada"""
    if len(lista) == 1:
        return 0
    elif len(lista) == 2:
        if lista[0] == item:
            return 0
        else:
            return 1
    else:
        index = len(lista)//2
        if lista[index] == item:
            if lista[index - 1] != lista[index]:
                return index
            else:
                if lista[0] == item:
                    return 0
                else:
                    while lista[index - 1] == lista[index]:
                        index -= 1
                    return index
        elif lista[index] > item:
            return index + 1 + busca(lista[index + 1:], item)
        else:
            return busca(lista[:index], item)


def main():
    # Cria uma lista de jogadores com as mãos de cada um
    n_de_jogadores = int(input())
    lista_de_jogadores = []
    for _ in range(n_de_jogadores):
        jogador = Jogador(input().split(", "))
        lista_de_jogadores.append(jogador)

    rodada_duvido = int(input())

    # Checa se há um ganhador
    ganhador = False
    pilha = []
    carta_força = Cartas("AO")
    rodada = 0
    while not (ganhador):
        """Começa o jogo"""
        for i in range(len(lista_de_jogadores)):
            print(f"Jogador {i + 1}")
            print(f"Mão: {' '.join([i.tipo_carta for i in lista_de_jogadores[i].mao])}")
        print("Pilha: ")

        for i in range(rodada_duvido):
            print(f"[Jogador {rodada % n_de_jogadores + 1}] ", end="")
            lista_de_jogadores[rodada % n_de_jogadores].discarta(
                pilha, carta_força
                )

            p = pilha.copy()
            ordena(p)
            carta_força = p[0]
            print(carta_força.numero)

            print("Pilha: ", end="")
            print(" ".join([i.tipo_carta for i in pilha]))
            if (lista_de_jogadores[rodada % n_de_jogadores].mao == [] and
               (rodada + 1) % rodada_duvido):
                print(f"Jogador {rodada % n_de_jogadores + 1} é o vencedor!")
                ganhador = True
                break
            rodada += 1

        # Entra na hora da dúvida
        if not (ganhador):
            print(f"Jogador {rodada % n_de_jogadores + 1} duvidou.")
            if pilha[-1].numero_value < carta_força.numero_value:
                for j in pilha:
                    lista_de_jogadores[(rodada - 1) % n_de_jogadores].mao.append(j)
                pilha = []
            else:
                for j in pilha:
                    lista_de_jogadores[rodada % n_de_jogadores].mao.append(j)
                pilha = []
            carta_força = Cartas("AO")
            ganhador_lista = [i.mao == [] for i in lista_de_jogadores]
            if any(ganhador_lista):
                for i in range(len(lista_de_jogadores)):
                    print(f"Jogador {i + 1}")
                    print(f"Mão: {' '.join([i.tipo_carta for i in lista_de_jogadores[i].mao])}")
                print("Pilha: ")
                for i in range(len(lista_de_jogadores)):
                    if lista_de_jogadores[i].mao == []:
                        jogador_ganhador = i + 1
                print(f"Jogador {jogador_ganhador} é o vencedor!")
                ganhador = True


main()
