def somaLista(valores=[]):
    """
    A função somaLista,rcebe uma lista de números e faz a soma de todos os 
    números a lista e retorna o resultado da soma
    
    Parameters
    ---------------------------
    valore: int[]
        Lista de números para a soma

    Returns
    -----------------------------
        Retorna a soma de uma lista
    """
    resultado = 0
    for i in valores:
        resultado+=i

    return resultado

def maiorValor(lista=[]):
    """
    A função maiorValor encontra o maior valor em uma lista numérica.

    Parameters
    -----------------------------
        lista: int[]

    Returns
    -----------------------------
        Retornas o maior valor da lista
    """
    m = lista[0]
    for i in lista:
        if i > m:
            m=i

    return m

def inverter(palavra=""):
    #Vamos utilizar o comando 
    #len(length-comprimento)para obter
    #a quantidade de caracteres da palavra
    qtd = len(palavra)
    invertida = ""
    for i in range (qtd -1, -1, -1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "É um palindromo"
    else:
        return "Não é um palindromo"
