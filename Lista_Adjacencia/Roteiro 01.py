#!/usr/bin/python
from grafo import Grafo

#vertice = [0], arestas = [1]
def Inicio():

    dicio = {}
    vertices = input("").split(", ") #Informe os vertices:

    arestas = input("").split(", ") #Informe as arestas:

    for i in range(len(arestas)):
        separando = arestas[i].split("(")

        tira_parenteses = separando[1].split(")")
        dicio[separando[0]] = tira_parenteses[0]

    return (vertices, dicio)

def Menu():
    print("Menu: \n"
          "\n a - Pares de Vértices não adjacentes: \n"
          " b - Vértice adjacente a ele mesmo: \n"
          " c - Há arestas paralelas: \n"
          " d - Informe o grau de vértice: \n"
          " e - Quais arestas incidem sobre o vértice: \n"
          " f - O grafo é completo: \n"
          " g - Desafio: \n"
          " h - Sair: \n")

def VerticesUsados(arestas):
    arestas = inicio[1].values()
    adjacente = []

    for j in arestas:
        palavra = j

        if (palavra[0] != palavra[2]) and palavra[0] not in adjacente:
            adjacente.append(palavra[0])
        if (palavra[2]) not in adjacente:
            adjacente.append(palavra[2])

    return adjacente

#Opcao a
def ParesAjacentes(vertices, arestas, adjacente) :
    vertices = inicio[0]
    arestas = inicio[1].values()
    adjacente = VerticesUsados(arestas)
    v_n_adj = ""

    for i in vertices:
        if i not in adjacente:
            v_n_adj += "\""
            v_n_adj += i
            v_n_adj += "\" "

    return v_n_adj

#Opcao b
def VerticeAdjacente(arestas):
    arestas = inicio[1].values()
    vertice_adjacente = 0

    for j in arestas:
        palavra = j

        if palavra[0] == palavra[2]:
            vertice_adjacente = 1

    if vertice_adjacente == 1:
        return True
    else:
        return False

#Opcao c
def ArestasParalelas(arestas, v_adjacente):
    arestas = inicio[1].values()
    v_adjacente = VerticesUsados(arestas)
    contador = 0

    for x in arestas:
        palavra = x

        for i in v_adjacente:
            for j in v_adjacente:
                contador += palavra.count((i + "-" + j))
                contador += palavra.count((j + "-" + i))
            if contador >= 2:
                return True
            else:
                contador = 0
        return False

#Opcao d
def GrauDoVertice(busca, arestas):
    vertice = busca
    arestas = inicio[1].values()
    adjacente = 0

    for j in arestas:
        palavra = j
        if vertice == palavra[0] and palavra[0] != palavra[2]:
            adjacente += 1

        if vertice == palavra[2] and palavra[2] != palavra[0]:
            adjacente += 1

    return str(adjacente)

#Opcao e
def ArestasIncidentes(busca, arestas):
    vertice = busca
    arestas = inicio[1].values()
    funcao = inicio[1].keys()
    adjacente = ""
    posicao = []

    for i in funcao:
        posicao.append(i)

    count = 0
    for j in arestas:
        palavra = j
        if vertice == palavra[0] and palavra[0] != palavra[2]:
            adjacente += "{"
            adjacente += posicao[count]
            adjacente += "}: "
            adjacente += palavra
            adjacente += "\n"

        if vertice == palavra[2] and palavra[2] != palavra[0]:
            adjacente += "{"
            adjacente += posicao[count]
            adjacente += "}: "
            adjacente += palavra
            adjacente += "\n "

        count += 1

    return adjacente

#Opcao f
def GrafoCompleto(arestas, v_adjacente ):
    arestas = inicio[1].values()
    v_adjacente = VerticesUsados(arestas)
    completo = False

    for x in v_adjacente:
        for z in v_adjacente:
            if (x + "-" + z) in arestas or (z + "-" + x) in arestas:
                completo = True
            elif x != z:
                completo = False
                break
    return completo

#Opcao g
def Desafio():
    print()


inicio = Inicio()
itens = ["a", "b", "c", "d", "e", "f", "g", "h"]
while True:

    menu = Menu()
    print("Informe uma letra: ")
    escolha = input().lower()
    grafo = Grafo(inicio[0], inicio[1])

    if escolha not in itens:
        print("\n\""+ escolha + "\" : Esta letra não esta no menu.\n")
    else:
        if escolha == "a" :
            verticePresentes = VerticesUsados(inicio[1])
            adjacente = ParesAjacentes(inicio[0], inicio[1], verticePresentes)
            print("Pares de Vértices não adjacentes:",adjacente + "\n")

        elif escolha == "b":
            laco = VerticeAdjacente(inicio[1])
            print("Vértice adjacente a ele mesmo:",laco, "\n")

        elif escolha == "c":
            verticePresentes = VerticesUsados(inicio[1])
            aParalelas = ArestasParalelas(inicio[1], verticePresentes)
            print("Há arestas paralelas: " + str(aParalelas) + "\n")

        elif escolha == "d":
            buscaG = input("Informe um vertice: ")
            grauVertice = GrauDoVertice(buscaG, inicio[1])
            print("Grau de vértice: " + grauVertice + "\n")

        elif escolha == "e":
            busca = input("Informe um vertice: ")
            aIncidentes = ArestasIncidentes(busca, inicio[1])
            print("Estas arestas incidem sobre o vértice: " + aIncidentes + "\n")

        elif escolha == "f":
            verticePresentes = VerticesUsados(inicio[1])
            completo = GrafoCompleto(inicio[1],verticePresentes)
            print("O grafo é completo: " + str(completo) + "\n")

        elif escolha == "g":
            desafio = Desafio()

        elif escolha == "h":
            break
