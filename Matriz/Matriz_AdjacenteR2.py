#!/usr/bin/python
from grafo import Grafo

#vertice = [0], dicionario_arestas = [1]
def Inicio():

    dicio = {}

    vertices = input().split(", ") #Informe os vertices:

    arestas = input().split(", ") #Informe as arestas:

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
          " h - Impressao da matriz: \n"
          " i - O Grafo é conexo (Warshall): \n"
          " j - Existe caminho Euleriano: \n"
          " x - Sair: \n")

#lista
def ListaDeArestas(aresta):
    aresta = aresta.values()
    listaA = []

    for i in aresta:
        listaA.append(i)
    return listaA

def VerticeIndice(vertice):
    indice_v = {}

    for i in range(len(vertice)):
        indice_v[i] = vertice[i]

    return indice_v

#matriz (bidirecional)
def MatrizAdjacencia(verticeindice, listadearestas):
    matriz = []

    for i in range(len(verticeindice.keys())):
        matriz.append([])
        for j in range(len(verticeindice.keys())):
            matriz[i].append(listadearestas.count((verticeindice[i] + "-" + verticeindice[j])) or listadearestas.count((verticeindice[j] + "-" + verticeindice[i])))

    return matriz

def ImpressaoMatriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("\n")

#Opcao a
def ParesAjacentes(matriz, vertice, listadearestas):
    completo = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0 and vertice[j] + "-" + vertice[i] not in listadearestas:
                completo.append((vertice[i] + "-" + vertice[j]))

    return completo

#Opcao b
def VerticeAdjacente(matriz):
    opcao = False

    for i in range(len(matriz)):
        if matriz[i][i] > 0:
            opcao = True
    return opcao

#Opcao c
def ArestasParalelas(matriz):
    aresta_paralela = False

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 1:
                aresta_paralela = True
    return aresta_paralela

#Opcao d
def GrauDoVertice(busca, verticeindice, vertice, matriz):
    adjacente = 0

    i = [i for i, v in verticeindice.items() if v == busca][0]

    for j in range(len(vertice)):
        adjacente += matriz [j][i]
        if j != i:
            adjacente  += matriz[i][j]
    return str(adjacente)

#Opcao e
def ArestasIncidentes(busca, vertice, matriz):
    l = []

    for i, v in enumerate(vertice):
        if busca == v:
            i_busca = i

    for x in range(len(matriz)):
        if matriz[i_busca][x] > 0:
            l.append(vertice[i_busca] + "-" + vertice[x])
        if matriz[x][i_busca] > 0 and x != i_busca:
            l.append(vertice[x] + "-" + vertice[i_busca])

    return l

#Opcao f
def GrafoCompleto(matriz):
    completo = True

    for x in range(len(matriz)):
        for z in range(len(matriz)):
            if matriz[x][z] == 0 and x != z:
                completo = False

    return completo

#Opcao g
def DesafioComprimento(vertices, matriz):                                                                                                                   #Bagaca so da raiva
    encontra_maior_caminho = 0

    for i in vertices:
        caminho = [[i]]

        while caminho:
            tam = caminho.pop(0)

            if encontra_maior_caminho < len(tam) - 1:
                encontra_maior_caminho = len(tam) - 1
            indice = vertices.index(tam[-1])

            for i, v in enumerate(vertices):
                if matriz[indice][i] != 0 and v not in tam:
                    caminho.append(tam + [v])

    return encontra_maior_caminho

def Warshall(matriz):
    matrizW = matriz

    for i in range(len(matrizW)):
        for j in range(len(matrizW)):
            if matrizW[i][j] == 1:
                for k in range(len(matrizW)):
                    if matrizW[j][k] != 0 or matrizW[i][k] != 0:
                        adicione = 1
                        matrizW[j][k] = adicione
                    else:
                        adicione = 0
                        matrizW[j][k] = adicione
    return matrizW

#Opcao i
def Conexo(warshall):
    conexo = bool

    for i in range(len(warshall)):
        for j in range(len(warshall)):
            if warshall[i][j] == 1:
                conexo = True
            else:
                conexo = False
                break

    return conexo

def EulerVertice():
    return 0

#opção j
def Euler(matriz, conexo):

    if conexo == False:
        print("\nNão existe caminho eureliano \n")

    else:
        total = 0
        i = 0

        while (total <= 2 and i < len(matriz)):
            grau = 0

            for j in range(len(matriz)):
                grau += matriz[i][j]
                grau += matriz[j][i]

            if grau % 2 == 1:
                total += 1
            i += 1

        if total > 2:
            print("\nNão existe caminho eureliano \n")
        else:
            print("\nExiste caminho eureliano \n")


inicio = Inicio()
itens = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "x"]

while True:

    try:

        grafo = Grafo(inicio[0], inicio[1])
        arestas = ListaDeArestas(inicio[1])
        verticesIndice = VerticeIndice(inicio[0])
        matriz =  MatrizAdjacencia(verticesIndice, arestas)
        warshall = Warshall(matriz)

        menu = Menu()
        escolha = input("Informe uma letra: ").lower()


        if escolha not in itens:
            print("\n\""+ escolha + "\" : Esta letra não esta no menu.\n")

        else:                                                                                                           #Informe os pares que não são adjacentes
            if escolha == "a" :
                adjacente = ParesAjacentes(matriz, inicio[0], arestas)
                print("Pares não adjacentes: " + str(adjacente) + "\n")

            elif escolha == "b":
                laco = VerticeAdjacente(matriz)
                print("Há algum laço: " + str(laco) + "\n")

            elif escolha == "c":
                aParalelas = ArestasParalelas(matriz)
                print("Há arestas paralelas: " + str(aParalelas) + "\n")

            elif escolha == "d":
                buscaG = input("Informe um vertice: ").upper()
                grauVertice = GrauDoVertice(buscaG, verticesIndice, inicio[0], matriz)
                print("Grau de vértice: " + str(grauVertice) + "\n")

            elif escolha == "e":
                busca = input("Informe um vertice: ").upper()
                aIncidentes = ArestasIncidentes(busca, inicio[0], matriz)
                print("Arestas incidentes do vertice " + busca + ": " + str(aIncidentes) + "\n")

            elif escolha == "f":
                completo = GrafoCompleto(matriz)
                print("O grafo é completo: " + str(completo) + "\n")

            elif escolha == "g":
                desafio = DesafioComprimento(inicio[0], matriz)
                print("O maior caminho é: " + str(desafio) + "\n")

            elif escolha == "h":
                impressao = ImpressaoMatriz(matriz)

            elif escolha == "i":
                impressao = ImpressaoMatriz(warshall)
                conexo = Conexo(warshall)
                print("O grafo é conexo: " + str(conexo) + "\n")

            elif escolha == "j":
                conexo = Conexo(warshall)
                euler = Euler(matriz, conexo)


            elif escolha == "x":
                break

    except:
        print("Informe valores válidos")
        inicio = Inicio()

