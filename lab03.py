players = int(input())  #Número de jogadores
drawn_numbers = input().split()  #Lista com os números retirados por cada jogador
intervals = input().split()     #Lista com os limites inferiores e superiores de cada jogador
 
points = []         #Lista vazia que vai receber a pontuação de cada jogador
 
for i in range(players):
    if i + 1 <= players/2 + 0.5:     #Vê se o jogador i está na primeira ou na segunda metade
        points.append((int(intervals[2 * i + 1]) - int(intervals[2 * i])) * int(drawn_numbers[i]))
    else:
        points.append(int(intervals[2 * i + 1]) - int(intervals[2 * i]) + int(drawn_numbers[i]))
 
position_points = []
winner = False
 
for i in range(len(points)):     #Checa qual foi a maior pontuação por meio de comparações. 
    position_points.append(0)
 
    for j in range(len(points)):
        if points[i] > points[j]:
                position_points[i] += 1       #Se uma pontuação é maior que a outra, ela ganha um ponto. 
             
    if position_points[i] == len(points) - 1:      #Se uma pontuação for a maior entre todas, ela vai ganhar todas as comparações, menos a com si mesma, ou seja, o tamanho da lista menos 1.
        print("O jogador número",i + 1,"vai receber o melhor bolo da cidade pois venceu com",points[i],"ponto(s)!")
        winner = True   #A variável winner detecra se houve uma pontuação maior que todas
 
if winner == False:     #Se não for detectado nenhuma pontuação que ganhe todas, houve um empate
     print("Rodada de cerveja para todos os jogadores!")
 
