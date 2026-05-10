import random

def multiplicacao_matrizes(matrix_1, matrix_2):
    resultado = []
    for i in range(len(matrix_1)):
        linha = []
        for j in range(len(matrix_2[0])):
            soma = 0
            for k in range(len(matrix_1[0])):
                soma += matrix_1[i][k] * matrix_2[k][j]
            linha.append(soma)
        resultado.append(linha)

    return resultado

def criptografia(palavra):
    lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    chave = [[4, 3], [1, 2]]
    x = [[], []]
    cont = 0
    par=True

    if len(palavra) % 2 == 1:
        palavra += "M"
        par=False

    for letra in palavra:
        if cont % 2 == 0:
            x[0].append(lista.index(letra))
        else:
            x[1].append(lista.index(letra))
        cont += 1
    matrix=multiplicacao_matrizes(chave,x)
    matrix=[[x%36 for x in row]for row in matrix]
    resultado=""
    for j in range(len(matrix[0])):
        resultado+=lista[matrix[0][j]]
        resultado+=lista[matrix[1][j]]
    if par==False:
        resultado += "G"
    return resultado


def descriptografia(palavra):
    lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    chave = [[58, -87], [-29, 116]]
    x = [[], []]
    cont = 0
    par=True
    if len(palavra) % 2 == 1:
        palavra =palavra[:-1]
        par=False
    for letra in palavra:
        if cont % 2 == 0:
            x[0].append(lista.index(letra))
        else:
            x[1].append(lista.index(letra))
        cont += 1
    matrix=multiplicacao_matrizes(chave,x)
    matrix=[[x%36 for x in row]for row in matrix]
    resultado=""
    for j in range(len(matrix[0])):
        resultado+=lista[matrix[0][j]]
        resultado+=lista[matrix[1][j]]
    if par==False:
        resultado=resultado[:-1]
    return resultado




