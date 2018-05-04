#!/usr/bin/python
from grafo import Grafo

#vertice = [0], arestas = [1]
def Inicio():

    dicio = {}

    vertices = input("Infome os vertices: ").split(", ") #Informe os vertices:

    arestas = input("Informe as arestas: ").split(", ") #Informe as arestas:

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
          " g - Maior caminho: \n"
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
def ParesAjacentes(vertices, arestas):
    vertices = inicio[0]
    arestas = inicio[1].values()
    completo = []
    resultado = " "

    for x in vertices:
        for z in vertices:
            if (x + "-" + z) not in arestas and (z + "-" + x) not in arestas :
                if x != z:
                    if (z + "-" + x) not in completo :
                        completo.append(x + "-" + z)
                        resultado += ("\n" + x + "-" + z)

    return resultado

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
    print(vertice)
    arestas = inicio[1].values()
    adjacente = 0

    for j in arestas:
        palavra = j
        if vertice == palavra[0] and palavra[0] != palavra[2]:
            adjacente += 1
            print(adjacente)

        if vertice == palavra[2] and palavra[2] != palavra[0]:
            adjacente += 1
            print(adjacente)

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

def DicionarioAdjacencia(vertices, arestas):
    arestas = inicio[1].values()
    dici = {}

    for i in vertices:
        dici[i] = set()

        for x in arestas:
            palavra = x
            if palavra[0] == i:
                dici[i].add(palavra[2])
            if palavra[2] == i:
                dici[i].add(palavra[0])
    return dici

def Comprimento(grafo, init, fim):                                                                                                                              # Algoritmo de busca Depth Dirst Search
    caminho = [(init, [init])]

    while caminho:
        (vertice, percorrer ) = caminho.pop()

        for o in grafo[vertice] - set(percorrer):
            if o == fim:
                yield percorrer + [o]
            else:
                caminho.append((o, percorrer + [o]))

#Opcao g
def DesafioComprimento(vertices, dicionario):                                                                                                                   #Bagaca so da raiva
    encontra_maior_caminho = 0
    for i in vertices:
        for j in vertices:
            if i != j:
                for c in list(Comprimento(dicionario, i, j)):
                    if len(c) - 1 > encontra_maior_caminho:
                        encontra_maior_caminho = len(c) - 1

    return encontra_maior_caminho


inicio = Inicio()
itens = ["a", "b", "c", "d", "e", "f", "g", "h"]

while True:

    try:

        grafo = Grafo(inicio[0], inicio[1])
        menu = Menu()
        print("Informe uma letra: ")
        escolha = input().lower()

        if escolha not in itens:
            print("\n\""+ escolha + "\" : Esta letra não esta no menu.\n")

        else:                                                                                                           #Informe os pares que não são adjacentes
            if escolha == "a" :
                adjacente = ParesAjacentes(inicio[0], inicio[1])
                print("Pares de Vértices não adjacentes:",adjacente + "\n")

            elif escolha == "b":
                laco = VerticeAdjacente(inicio[1])
                print("Vértice adjacente a ele mesmo:",laco, "\n")

            elif escolha == "c":
                verticePresentes = VerticesUsados(inicio[1])
                aParalelas = ArestasParalelas(inicio[1], verticePresentes)
                print("Há arestas paralelas: " + str(aParalelas) + "\n")

            elif escolha == "d":
                buscaG = input("Informe um vertice: ").upper()
                grauVertice = GrauDoVertice(buscaG, inicio[1])
                print("Grau de vértice: " + grauVertice + "\n")

            elif escolha == "e":
                busca = input("Informe um vertice: ").upper()
                aIncidentes = ArestasIncidentes(busca, inicio[1])
                print("Estas arestas incidem sobre o vértice: " + aIncidentes + "\n")

            elif escolha == "f":
                verticePresentes = VerticesUsados(inicio[1])
                completo = GrafoCompleto(verticePresentes, inicio[1])
                print("O grafo é completo: " + str(completo) + "\n")

            elif escolha == "g":
                verticePresente = VerticesUsados(inicio[1])
                listaadjacente =  DicionarioAdjacencia(verticePresente, inicio[1])
                desafio = DesafioComprimento(verticePresente, listaadjacente)
                print("O maior caminho é: " + str(desafio) + "\n")

            elif escolha == "h":
                break

    except:
        print("Informe valores válidos")
        inicio = Inicio()