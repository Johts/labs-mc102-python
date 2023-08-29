def find_winner(categories: list) -> str:
    """Acha a maior pontuação em uma listas de listas"""
 
    winner = categories[0]
 
    for i in range(len(categories) - 1):
        if categories[i + 1][1] > winner[1]:
            winner = categories[i + 1]
        elif categories[i + 1][1] == winner[1]:
            if categories[i + 1][2] > winner[2]:
                winner = categories[i + 1]
 
    return winner[0]
 
 
num_de_filmes = int(input())  # Pega o número de filmes que serão avaliados
lista_de_filmes = []
for i in range(num_de_filmes): 
    lista_de_filmes.append(input())  # Cria a lista dos filmes 
  
num_de_avaliacoes = int(input())  # Pega o número de avaliações 
avaliacoes = [] 
for i in range(num_de_avaliacoes): 
    # Avaliações no formato: 
    # avaliador, categoria, filme, nota 
    avaliacoes.append(input().split(", ")) 
categorias = (
    "filme que causou mais bocejos",
    "filme que foi mais pausado",
    "filme que mais revirou olhos",
    "filme que não gerou discussão nas redes sociais",
    "enredo mais sem noção"
    )
 
# Cria um dicionário onde vão estar as pontuações dos filmes em cada categoria
# A chave i é a categoria, j é cada filme
# 0, 0 são respectivamente a pontuação e o número de avaliações
pontuacoes = {i: [[j, 0, 0] for j in lista_de_filmes] for i in categorias}
nao_merecia = "sem ganhadores"
"""
i[0] = avaliador
i[1] = categoria avaliada
i[2] = filme avaliado
i[3] = pontuação que foi avaliada
pontuacoes = {categoria: [[filme1, 0, 0], [filme2, 0, 0]...]}
"""
 
# Adiciona a pontuação de cada filme e o n de avaliações 
for i in avaliacoes: 
    for j in range(len(lista_de_filmes)): 
        if i[2] == pontuacoes[i[1]][j][0]: 
            pontuacoes[i[1]][j][1] += int(i[3]) 
            pontuacoes[i[1]][j][2] += 1 
  
# Faz a média das pontuações dividindo a pontuação pelo n de avaliações 
for i in categorias: 
    for j in range(len(lista_de_filmes)): 
        try: 
            pontuacoes[i][j][1] /= pontuacoes[i][j][2] 
        except ZeroDivisionError: 
            pass 
  
# Cria uma variável que receberá: 
# O número de avaliações de cada filme e quantas categorias ganhou 
premiacoes_especiais = {i: [0, 0] for i in lista_de_filmes} 
for i in pontuacoes: 
    for j in pontuacoes[i]: 
        premiacoes_especiais[j[0]][0] += j[2] 
  
# Resultados das premiações 
print("#### abacaxi de ouro ####\n") 
print("categorias simples") 
for i in categorias: 
    print("categoria:", i) 
    print("- {}".format(find_winner(pontuacoes[i]))) 
    premiacoes_especiais[find_winner(pontuacoes[i])][1] += 1 
  
pior_filme = lista_de_filmes[0] 
  
for i in range(len(lista_de_filmes) - 1): 
    if premiacoes_especiais[lista_de_filmes[i + 1]][1] > premiacoes_especiais[pior_filme][1]: 
        pior_filme = lista_de_filmes[i + 1] 
    # Caso de empate: 
    elif premiacoes_especiais[lista_de_filmes[i + 1]][1] == premiacoes_especiais[pior_filme][1]: 
        # Calcula a soma das médias 
        sum = [0, 0] 
        for j in categorias: 
            for f in range(len(lista_de_filmes)): 
                if pontuacoes[j][f][0] == lista_de_filmes[i + 1]: 
                    sum[0] += pontuacoes[j][f][1] 
                elif pontuacoes[j][f][0] == pior_filme: 
                    sum[1] += pontuacoes[j][f][1] 
        # Checa qual a maior média 
        if sum[0] > sum[1]: 
            pior_filme = lista_de_filmes[i + 1] 
  
# Lista de filmes que não tiveram avaliações
nao_merecia_lista = [i for i in lista_de_filmes if premiacoes_especiais[i][0] == 0]
# Transforma em uma string para impressão
if len(nao_merecia_lista) == 0:
    nao_merecia_lista = "sem ganhadores"
else:
    nao_merecia_lista = ", ".join(nao_merecia_lista)
 
print("\ncategorias especiais")
print("prêmio pior filme do ano")
print("- {}".format(pior_filme))
print("prêmio não merecia estar aqui")
print("- {}".format(nao_merecia_lista))
