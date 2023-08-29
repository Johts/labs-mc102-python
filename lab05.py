def mostrar(code):
    """Mostra o código"""
    str = ""
    for i in code:
        str += i
    print(str)
 
def transpor(code, i, j, k):
    if j < len(code) and i < len(code): #Regra 3 e 4, nenhuma alteração será feita se j ou i for maior que o código
        if k >= len(code):
            k = len(code)
        """Transpõe uma seção do código i > j por uma j+1 > k e vice-versa"""
        list_code = [code[:i],code[j+1:k+1],code[i:j+1],code[k+1:]] #Divide o código nos índices indicados e os troca, mudando o 2º e 3º itens da lista
 
        code = [] 
        for m in list_code: #Transforma o código dividido em uma só lista
            for f in m:
                code.append(f)
        return code
 
def combinar(code, sequence, i):
    """Combina uma sequência g no código, a partir do índice i"""
    g_list = [f for f in sequence] #Transforma a sequência em uma lista
    list_code = [code[:i],g_list,code[i:]] #Insere a sequência em uma lista dividida
    code = []
    for m in list_code: #Transforma a lista dividida em uma normal
        for f in m:
            code.append(f)
    return code
 
def reverter(code, i, j):
    """Reverte uma sequência dentro de um código, do i elemento até o j"""
    if i < len(code): #Regra 3, se i na reversão for maior que o tamanho do código nada acontecerá
        code_backup = list(code)
        for l in range(i, j + 1):
            code[l] = code_backup[j + i - l] 
        return code
 
def concatenar(code, sequence):
    """Concatena uma sequência ao código"""
    for i in sequence: 
        code.append(i)
    return code
 
def buscar(code, sequence):
    """Busca uma determinada sequência no código"""
    code_str = ""
    for i in code: #Transforma o código em uma string
        code_str += i
 
    return len(code_str.split(sequence)) - 1 #Quebra a string usando o método split(), que terá n + 1 elementos para cada n aparições da sequência no código
 
def buscar_bidirecional(code, sequence):
    code_backup = list(code)
    """Busca uma determinada sequência no código e no seu reverso"""
    return buscar(code_backup, sequence) + buscar(reverter(code_backup, 0, len(code_backup) - 1), sequence)
 
def remover(code, i, j):
    if i < len(code): #Regra 3, se i na reversão for maior que o tamanho do código nada acontecerá
        """Remove uma sequência de i até j do código"""
        list_code = [code[:i],code[j+1:]] #Retira a sequência code[i:j+1] correspondente à sequência de i até j
        code = []
        for m in list_code:
            for f in m:
                code.append(f)
        return code
 
def transpor_e_reverter(code, i, j, k):
    """Transpõe as subseções i > j e j+1 > k e reverte elas"""  
    if j < len(code) and i < len(code) and j != i: #Regra 3 e 4, nenhuma alteração será feita se j ou i for maior que o código
        list_code = [code[:i], reverter(code[i:j+1], 0, len(code[i:j+1]) - 1), reverter(code[j+1:k+1], 0, len(code[j+1:k+1]) - 1), code[k+1:]] #Divide o código nos índices indicados e os troca, mudando o 2º e 3º itens da lista e os revertendo
 
        code = [] 
        for m in list_code: #Transforma o código dividido em uma só lista
            for f in m:
                code.append(f)
    return code
 
#Começo da execução do código
run = True
genoma = [i for i in input()]
while run:
    comando = input()
    parametros = comando.split()
    for i in range(len(parametros)):
        if parametros[i].isnumeric():
            parametros[i] = int(parametros[i])
 
            if parametros[i] >= len(genoma) and parametros[i] != 0: #Regra 2, se os parâmetros forem maiores que o código, o maior índice válido deverá ser usado
                parametros[i] = len(genoma) - 1
            
            if parametros[i] < 0: #Regra 1, parâmetros devem ser inteiros não negativos
                raise Exception("Parâmetros numéricos devem ser inteiros não negativos")
    if comando == "mostrar":
        mostrar(genoma)
 
    elif "buscar_bidirecional" in comando:
        print(buscar_bidirecional(genoma, parametros[1]))
 
    elif "buscar" in comando:
        print(buscar(genoma, parametros[1]))
    
    elif "transpor_e_reverter" in comando:
        genoma = transpor_e_reverter(genoma, parametros[1], parametros[2], parametros[3])
 
    elif "reverter" in comando:
        genoma = reverter(genoma, parametros[1], parametros[2])
    
    elif "concatenar" in comando:
        genoma = concatenar(genoma, parametros[1])
    
    elif "transpor" in comando:
        genoma = transpor(genoma, parametros[1] ,parametros[2], parametros[3])  
    
    elif "remover" in comando:
        genoma = remover(genoma, parametros[1], parametros[2])
 
    elif "combinar" in comando:
        genoma = combinar(genoma, parametros[1], parametros[2])
 
    elif comando == "sair":
        run = False
