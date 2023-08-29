days = int(input()) #Número de dias
 
for i in range(days): #Loop que roda a cada dia passado
    fighting_animals = int(input()) #Número de pares de animais que brigam
    fighting_pairs = []
 
    for j in range(fighting_animals): #Cria uma lista de listas contendo os pares que brigam
        fighting_pairs.append(input().split())
 
    procedures = input().split() #Lista de procedimentos disponíveis
    for j in range(len(procedures)//2): #Converte o número de procedimentos disponíveis em int
        procedures[2*j+1] = int(procedures[2*j+1])
    present_animals = int(input()) #Número de animais no dia
    animal_procedures = []
    
    for j in range(present_animals): #Cria uma lista de procedimentos e animais que solicitaram-os
        animal_procedures.append(input().split())
    
    brigas = 0
    for j in fighting_pairs: #Loop que checa se existe um par de animais que briga ou não
        b = 0
        for k in animal_procedures:
            if j[0] == k[0] or j[1] == k[0]: #Se um animal que briga de um determinado par estiver presente, b ganha 1, 
                b += 1
        if b >= 2: #Se os dois animais brigantes estiverem presentes,  b = 2 e existe uma briga.
            brigas += 1
    #Listas vazias que irão receber os animais que foram, não foram ou solicitaram procedimentos inexistentes
    attended_animals = [] #Animais atendidos
    unattended_animals = [] #Animais não atendidos
    unexistent_procedures = [] #Animais que solicitaram procedimentos que não existem
 
    for j in range(present_animals): #Checa se um animal foi atendido, não foi, ou solicitou um procedimento que não existe
        b = 0
        for k in range(len(procedures)//2):
            if animal_procedures[j][1] == procedures[2*k]: #Se o animal solicitou um procedimento que existe:
                if procedures[2*k+1] > 0: #Checa se ainda existem procedimentos disponíveis
                    procedures[2*k+1] -= 1
                    attended_animals.append(animal_procedures[j][0])
                else: 
                    unattended_animals.append(animal_procedures[j][0])
            else:
                b += 1 #Se o procedimento solicitado não for igual ao procedimento testado, b aumenta 1.
        if b == len(procedures)//2: #Se o procedimento não for igual a nenhum dos testados, b vai ser igual ao número de testes, e esse procedimento não existe
            unexistent_procedures.append(animal_procedures[j][0])
 
    #Procedimentos para tornar a lista de animais atendidos ou não em strings formatadas para o print no final do loop
    attended_string = ""
    unattended_string = ""
 
    if len(attended_animals) > 0:
        attended_string += attended_animals[0]
    if len(unattended_animals) > 0:
        unattended_string += unattended_animals[0]
 
    for j in range(len(attended_animals) - 1): 
        attended_string += ", " + attended_animals[j + 1]
    for j in range(len(unattended_animals) - 1):
        unattended_string +=  ", " + unattended_animals[j + 1]
    
    
    
    #Conclusão do dia, print dos resultados:
    print("Dia:", i + 1)
    print("Brigas:", brigas)
    if len(attended_animals) > 0:
        print("Animais atendidos:", attended_string)
    if len(unattended_animals) > 0:
        print("Animais não atendidos:", unattended_string)
    for j in unexistent_procedures:
        print("Animal",j,"solicitou procedimento não disponível.")
    print()
