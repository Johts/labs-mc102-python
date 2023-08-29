print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")
print("Seu SO anterior era Linux?")
print("(0) Não")
print("(1) Sim")
fstchoice = input()
 
motivpath = "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são:" 
chlngpath = "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições:" 
learnpath = "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são:"
 
if fstchoice == "0":
    print("Seu SO anterior era um MacOS?")
    print("(0) Não")
    print("(1) Sim")
    scndchoice = input()
    if scndchoice == "0":
        distros = "Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro."
        print(motivpath,distros)
    elif scndchoice == "1":
        distros = "ElementaryOS, ApricityOS."
        print(motivpath,distros)
    else:
        print("Opção inválida, recomece o questionário.")
elif fstchoice == "1":
    print("É programador/ desenvolvedor ou de áreas semelhantes?")
    print("(0) Não")
    print("(1) Sim")
    print("(2) Sim, realizo testes e invasão de sistemas")
    scndchoice = input()
    if scndchoice == "0":
        distros = "Ubuntu Mint, Fedora."
        print(learnpath,distros)
    elif scndchoice == "2":
        distros = "Kali Linux, Black Arch."
        print(learnpath,distros)
    elif scndchoice == "1":
        print("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?")
        print("(0) Não")
        print("(1) Sim")
        thrdchoice = input()
        if thrdchoice == "0":
            print("Já utilizou Arch Linux?")
            print("(0) Não")
            print("(1) Sim")
            frthchoice = input()
            if frthchoice == "0":
                distros = "Antergos, Arch Linux."
                print(learnpath, distros)
            elif frthchoice == "1":
                distros = "Gentoo, CentOS, Slackware."
                print(chlngpath,distros)
            else:
                print("Opção inválida, recomece o questionário.")
        elif thrdchoice == "1":
            print("Já utilizou Debian ou Ubuntu?")
            print("(0) Não")
            print("(1) Sim")
            frthchoice = input()
            if frthchoice == "0":
                distros = "OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu."
                print(learnpath, distros)
            elif frthchoice == "1":
                distros = "Manjaro, ApricityOS."
                print(chlngpath,distros)
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    else:
        print("Opção inválida, recomece o questionário.")
else:
    print("Opção inválida, recomece o questionário.")
