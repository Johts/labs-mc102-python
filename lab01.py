schoice = input() 
rchoice = input() 
  
sheilawin = False 
reginwin = False 
 
if schoice == "lagarto":
    if rchoice == "spock" or rchoice == "papel":
        sheilawin = True
    elif rchoice == "pedra" or rchoice == "tesoura":
        reginwin = True
elif schoice == "spock":
    if rchoice == "tesoura" or rchoice == "pedra":
        sheilawin = True
    elif rchoice == "lagarto" or rchoice == "papel":
        reginwin = True
elif schoice == "papel":
    if rchoice == "spock" or rchoice == "pedra":
        sheilawin = True
    elif rchoice == "lagarto" or rchoice == "tesoura":
        reginwin = True
elif schoice == "tesoura":
    if rchoice == "lagarto" or rchoice == "papel":
        sheilawin = True
    elif rchoice == "pedra" or rchoice == "spock":
        reginwin = True
elif schoice == "pedra":
    if rchoice == "tesoura" or rchoice == "lagarto":
        sheilawin = True
    elif rchoice == "papel" or rchoice == "spock":
        reginwin = True
 
if sheilawin == True:
    print("Interestelar")
elif reginwin == True:
    print("Jornada nas Estrelas")
else:
    print("empate")
