class Mapa():
    """Cria uma classe de Mapas"""
    def __init__(self, dimensoes: tuple):
        self._dimensoes = dimensoes
        self._mapa_matriz = [["." for j in range(self.dimensoes[1])]
                             for i in range(self.dimensoes[0])]

    @property
    def dimensoes(self):
        return self._dimensoes

    @property
    def mapa_matriz(self):
        return self._mapa_matriz

    @mapa_matriz.setter
    def mapa_matriz(self, novo_mapa: list):
        self._mapa_matriz = novo_mapa

    def __str__(self):
        str = ""
        for i in self.mapa_matriz:
            str += " ".join(i) + "\n"
        return str

    def atualizar_mapa(self, objetos_presentes: dict):
        self.mapa_matriz = [["." for j in range(self.dimensoes[1])]
                            for i in range(self.dimensoes[0])]
        for i in objetos_presentes:
            self.mapa_matriz[i.posicao[0]][i.posicao[1]] = i.tipo


class Personagem:
    """Cria uma classe de seres humanóides(monstros e o personagem)"""

    def __init__(self, posicao: list, vida: int, dano: int):
        self._posicao = posicao
        self._vida = vida
        self._dano = dano
        self._tipo = "P"
        self._volta = False

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, posicao: list):
        if posicao[0] >= 0:
            self._posicao[0] = posicao[0]
        if posicao[1] >= 0:
            self._posicao[1] = posicao[1]

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida: int):
        if vida >= 0:
            self._vida = vida
        else:
            self._vida = 0

    @property
    def dano(self):
        return self._dano

    @dano.setter
    def dano(self, n_dano: int):
        if n_dano >= 1:
            self._dano = n_dano
        else:
            self._dano = 1

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def volta(self):
        return self._volta

    @volta.setter
    def volta(self, n):
        self._volta = n

    def __str__(self):
        return (f"O personagem tem {self.vida} de vida, " +
                f"{self.dano} de dano, e está na posição {self.posicao}")

    def mover_personagem(self, map_dimensions: list):

        if self.posicao[0] == map_dimensions[0] - 1:
            self.volta = True

        if self.posicao[0] != map_dimensions[0] - 1 and not self.volta:
            self.posicao[0] += 1
        elif self.posicao[0] % 2 == 0:
            if self.posicao[1] == 0:
                self.posicao[0] -= 1
            else:
                self.posicao[1] -= 1
        else:
            if self.posicao[1] == map_dimensions[1] - 1:
                self.posicao[0] -= 1
            else:
                self.posicao[1] += 1

    def vivo(self):
        if self.vida > 0:
            return True
        else:
            return False


class Monstro(Personagem):
    """Classe Monstro que herda da classe Personagem"""

    def __init__(self, posicao: list, vida: int, dano: int, tipo: str):
        super().__init__(posicao, vida, dano)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return (f"O monstro tem {self.vida} de vida, {self.dano} de dano," +
                f" está na posição {self.posicao} e é do tipo {self.tipo} ")

    def mover_personagem(self, map_dimensions):
        if self.tipo == "U":
            if self.posicao[0] > 0:
                self.posicao[0] -= 1
        elif self.tipo == "D":
            if self.posicao[0] < map_dimensions[0] - 1:
                self.posicao[0] += 1
        elif self.tipo == "L":
            if self.posicao[1] > 0:
                self.posicao[1] -= 1
        elif self.tipo == "R":
            if self.posicao[1] < map_dimensions[1] - 1:
                self.posicao[1] += 1


class Objeto:
    """Cria uma classe de objetos que podem ser adquiridos pelo Link"""

    def __init__(self, nome: str, tipo: str,
                 posicao: list, status: int):
        self._nome = nome
        self._tipo = tipo
        self._posicao = posicao
        self._status = status

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, coordenadas: list):
        self._posicao = coordenadas

    @property
    def status(self):
        return self._status

    def __str__(self):
        return (f"O objeto {self.nome} é de {self.tipo}, " +
                f"está na posição {self.posicao} e tem valor {self.status}")


class Saida:
    def __init__(self, posicao: list):
        self._posicao = posicao
        self._tipo = "*"

    @property
    def posicao(self):
        return self._posicao

    @property
    def tipo(self):
        return self._tipo


def input_inteiro(split=" ") -> list:
    """Retorna uma lista de números convertidos em inteiro"""

    return [int(i) if (i.isnumeric() or i[1:].isnumeric()) else i
            for i in input().split(split)]


def main():
    # Pega os dados do personagem
    dados_personagem = input_inteiro()

    # Cria o mapa inicial
    mapa_dimen = input_inteiro()
    mapa_do_jogo = Mapa(mapa_dimen)

    # Retorna a posição inicial do Link
    pos_init = input_inteiro(",")

    # Retorna a posição de saída do mapa
    saida = [i for i in input_inteiro(",")]
    saida_obj = Saida(saida)
    obj_dict = {}

    n_monstros = int(input())

    # Cria uma lista de monstros
    lista_de_monstros = []
    for i in range(n_monstros):
        dados_m = input_inteiro()
        pos = [int(i) for i in dados_m[3].split(",")]
        monstro = Monstro(pos, dados_m[0],
                          dados_m[1], dados_m[2])
        lista_de_monstros.append(monstro)
    n_objetos = int(input())

    # Cria uma lista de objetos
    lista_de_objetos = []
    for i in range(n_objetos):
        dados_objeto = input_inteiro()
        pos = [int(i) for i in dados_objeto[2].split(",")]
        objeto = Objeto(dados_objeto[0], dados_objeto[1],
                        pos, dados_objeto[3])
        lista_de_objetos.append(objeto)

    link = Personagem(pos_init, dados_personagem[0], dados_personagem[1])
    # Cria um dicionário de objetos para representar no mapa
    for i in lista_de_objetos:
        obj_dict[i] = i.posicao
    for i in lista_de_monstros:
        obj_dict[i] = i.posicao
    obj_dict[saida_obj] = saida_obj.posicao
    obj_dict[link] = link.posicao

    mapa_do_jogo.atualizar_mapa(obj_dict)
    print(mapa_do_jogo)

    # Loop principal do jogo
    while link.posicao != saida and link.vivo():
        link.mover_personagem(mapa_do_jogo.dimensoes)
        for j in lista_de_monstros:
            if j.vivo():
                j.mover_personagem(mapa_do_jogo.dimensoes)

        for objeto in lista_de_objetos:
            # Checa se Link está na mesma posição que um objeto
            if link.posicao == objeto.posicao:
                if objeto.tipo == "v":
                    link.vida += objeto.status
                    print(f"[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome}" +
                          f" com status de {objeto.status}")

                elif objeto.tipo == "d":
                    link.dano += objeto.status
                    print(f"[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome}" +
                          f" com status de {objeto.status}")

                objeto.tipo = "."

        for monstro in lista_de_monstros:
            # Checa se Link está na mesma posição que um monstro
            if link.posicao == monstro.posicao and link.vivo():
                if link.dano >= monstro.vida:
                    dano_str = monstro.vida
                else:
                    dano_str = link.dano

                monstro.vida -= link.dano

                print(f"O Personagem deu {dano_str} de dano ao " +
                      f"monstro na posicao ({monstro.posicao[0]}, {monstro.posicao[1]})")
                if monstro.vivo():
                    if monstro.dano >= link.vida:
                        dano_str = link.vida
                    else:
                        dano_str = monstro.dano

                    link.vida -= monstro.dano

                    print(f"O Monstro deu {dano_str} de dano ao " +
                          f"Personagem. Vida restante = {link.vida}")
                else:
                    monstro.tipo = "."

        if not link.vivo():
            link.tipo = "X"

        mapa_do_jogo.atualizar_mapa(obj_dict)
        print(mapa_do_jogo)

        if link.posicao == saida_obj.posicao:
            print("Chegou ao fim!")


main()
