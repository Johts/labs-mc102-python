def descripto(text: str, key: int) -> str:
    """Descriptografa uma string revertendo a chave key"""
 
    descript_string = ""
    for i in text:  # Transforma o caractere com a chave
        # Módulo que lida com over e underflow
        descript_string += chr((ord(i) + key - 32) % 95 + 32)
    return descript_string
 
 
def vowel_finder(text: str) -> int:
    """Acha a primeira vogal em um determinado texto"""
 
    vogais = "AEIOUaeiou"
    for i in range(len(text)):
        for j in vogais:
            if text[i] == j:
                return i
 
 
def consonant_finder(text: str) -> int:
    """Acha a primeira consoante em um determinado texto"""
 
    consoantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    for i in range(len(text)):
        for j in consoantes:
            if text[i] == j:
                return i
 
 
def number_finder(text: str) -> int:
    """Acha o primeiro numeral em um determinado texto"""
 
    numeros = "0123456789"
    for i in range(len(text)):
        for j in numeros:
            if text[i] == j:
                return i
 
 
def key_finder(text: str, operator: str, operand1: str, operand2: str) -> str:
    """Acha a chave de um texto dado seu operando e as posições de interesse"""
 
    if operand1 == "vogal":  # Checa o tipo de procura para o operando 1
        p1 = vowel_finder(text)
    elif operand1 == "consoante":
        p1 = consonant_finder(text)
    elif operand1 == "numero":
        p1 = number_finder(text)
    else:
        for i in range(len(text)):
            if text[i] == operand1:
                p1 = i
                break
 
    if operand2 == "vogal":  # Checa o tipo de procura para o operando 2
        p2 = vowel_finder(text[p1:]) + p1
    elif operand2 == "consoante":
        p2 = consonant_finder(text[p1:]) + p1
    elif operand2 == "numero":
        p2 = number_finder(text[p1:]) + p1
    else:
        for i in range(len(text[p1:])):
            if text[p1:][i] == operand2:
                p2 = i + p1
                break
 
    string = str(p1) + operator + str(p2)
    return eval(string)
 
 
operador = input()
operando1 = input()
operando2 = input()
linhas = int(input())
lista_texto = []
for i in range(linhas):
    lista_texto.append(input())
 
texto_uma_linha = ""
for i in lista_texto:
    texto_uma_linha += i
 
# Acha a chave considerando o texto em uma linha só
chave = key_finder(texto_uma_linha, operador, operando1, operando2)
 
print(chave)
for i in range(linhas):
    print(descripto(lista_texto[i], chave))
