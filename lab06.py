def soma_vetores(n1: list[int], n2: list[int]) -> list[int]:
    """Soma dois vetores n1 e n2"""
 
    # Converte o menor vetor para o tamanho do maior, adicionando 0s no final
    if len(n1) < len(n2): 
        for i in range(len(n2) - len(n1)): 
            n1.append(0) 
    else: 
        for i in range(len(n1) - len(n2)): 
            n2.append(0) 
 
    sum = []
    for i in range(len(n2)):
        sum.append(n1[i] + n2[i])
    return sum
 
 
def subtrai_vetores(n1: list[int], n2: list[int]) -> list[int]:
    """Subtrai dois vetores n1 e n2"""
 
    neg_n2 = [-i for i in n2]  # Transforma n2 em negativo
    return soma_vetores(n1, neg_n2)  # Soma de n1 e o negativo de n2
 
 
def multiplica_vetores(n1: list[int], n2: list[int]) -> list[int]:
    """Multiplica dois vetores n1 e n2"""
 
    # Converte o menor vetor para o tamanho do maior, adicionando 1s no final
    if len(n1) < len(n2):
        for i in range(len(n2) - len(n1)):
            n1.append(1)
    else:
        for i in range(len(n1) - len(n2)):
            n2.append(1)
 
    mult = []
    for i in range(len(n2)):
        mult.append(n1[i] * n2[i])
    return mult
 
 
def divide_vetores(n1: list[int], n2: list[int]) -> list[int]:
    """Divide dois vetores n1 e n2"""
 
    # Converte o menor vetor para o tamanho do maior
    if len(n1) < len(n2):
        for i in range(len(n2) - len(n1)):
            # Adiciona 0s no final se o primeiro vetor for menor
            n1.append(0)
    else:
        for i in range(len(n1) - len(n2)):
            # Adiciona 1s no final se o segundo vetor for menor
            n2.append(1)
 
    divide = []
    for i in range(len(n2)):
        divide.append(n1[i] // n2[i])
    return divide
 
 
def multiplicacao_escalar(n1: list[int], e: int) -> list[int]:
    """Multiplica o vetor n1 pelo escalar e"""
 
    mult_escalar = []
    for i in range(len(n1)):
        mult_escalar.append(n1[i] * e)
    return mult_escalar
 
 
def n_duplicacao(n1: list[int], n: int) -> list[int]:
    """Copia o vetor n1 n vezes"""
 
    duplicated_vector = []
    for _ in range(n):
        for i in n1: 
            duplicated_vector.append(i) 
    return duplicated_vector
 
 
def soma_elementos(n1: list[int]) -> int:
    """Soma todos os elementos do vetor n1"""
 
    summation = 0
    for i in n1:
        summation += i
    return summation
 
 
def produto_interno(n1: list[int], n2: list[int]) -> int:
    """Faz o produto de cada elemento dos vetores n1 e n2 e os soma"""
 
    # Converte o menor vetor para o tamanho do maior, adicionando 1s no final
    if len(n1) < len(n2):
        for i in range(len(n2) - len(n1)):
            n1.append(1)
    else:
        for i in range(len(n1) - len(n2)):
            n2.append(1)
 
    in_product = 0
    for i in range(len(n1)): 
        in_product += n1[i] * n2[i] 
    return in_product
 
 
def multiplica_todos(n1: list[int], n2: list[int]) -> list[int]:
    """Multiplica cada elemento de um vetor com todos do outro vetor"""
 
    total_mult = []
    for i in n1:
        local_sum = 0
        for j in n2:
            # Multiplicação de i do vetor n1 com todos os elementos de n2
            local_sum += i * j
        total_mult.append(local_sum)
    return total_mult
 
 
def correlacao_cruzada(n1: list[int], mask: list[int]) -> list[int]:
    """Calcula a correlação cruzada entre n1 e a máscara mask"""
 
    cross_correlation = []
    for i in range(len(n1) - len(mask) + 1):
        local_sum = 0
        for j in range(len(mask)):
            # Calcula o produto interno para a posição i 
            local_sum += n1[i + j] * mask[j] 
        cross_correlation.append(local_sum)
    return cross_correlation
 
 
def get_vector2() -> list[int]:
    """Função que recebe um segundo vetor para funções que necessitam"""
 
    vetor_ = input().split(",")
    vetor2 = [int(i) for i in vetor_]
    return vetor2
 
 
def main() -> None:
    """"Função principal do código"""
 
    run = True
    vetor0 = input().split(",")  # Recebe o vetor1 do usuário em forma de str
    vetor1 = [int(i) for i in vetor0]  # Converte os elementos do vetor1 em int
 
    while run:  # Loop que irá rodar até o usuário digitar fim
        comando = input()
 
        if comando == "soma_vetores":
            vetor2 = get_vector2()
            vetor1 = soma_vetores(vetor1, vetor2)
            print(vetor1)
        elif comando == "subtrai_vetores":
            vetor2 = get_vector2()
            vetor1 = subtrai_vetores(vetor1, vetor2)
            print(vetor1)
        elif comando == "multiplica_vetores":
            vetor2 = get_vector2()
            vetor1 = multiplica_vetores(vetor1, vetor2)
            print(vetor1)
        elif comando == "divide_vetores":
            vetor2 = get_vector2()
            vetor1 = divide_vetores(vetor1, vetor2)
            print(vetor1)
        elif comando == "multiplicacao_escalar":
            escalar = int(input())
            vetor1 = multiplicacao_escalar(vetor1, escalar)
            print(vetor1)
        elif comando == "n_duplicacao":
            n = int(input())
            vetor1 = n_duplicacao(vetor1, n)
            print(vetor1)
        elif comando == "soma_elementos":
            vetor1 = [soma_elementos(vetor1)]
            print(vetor1)
        elif comando == "produto_interno":
            vetor2 = get_vector2()
            vetor1 = [produto_interno(vetor1, vetor2)]
            print(vetor1)
        elif comando == "multiplica_todos":
            vetor2 = get_vector2()
            vetor1 = multiplica_todos(vetor1, vetor2)
            print(vetor1)
        elif comando == "correlacao_cruzada":
            mascara = get_vector2()
            vetor1 = correlacao_cruzada(vetor1, mascara)
            print(vetor1)
        elif comando == "fim":
            run = False
 
 
if __name__ == "__main__":
    main()
