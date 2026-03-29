import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    distancia = {node: float('inf') for node in graph}
    distancia[start] = 0
    nodos_visitados = set()
    nodos_precedentes = {node: None for node in graph}

    while nodos_visitados != set(graph):
        nodo_actual = min(
            (node for node in graph if node not in nodos_visitados),
            key=lambda node: distancia[node]
        )

        nodos_visitados.add(nodo_actual)

        for vecino, peso in graph[nodo_actual].items():
            if vecino not in nodos_visitados:
                nueva_distancia = distancia[nodo_actual] + peso
                if nueva_distancia < distancia[vecino]:
                    distancia[vecino] = nueva_distancia
                    nodos_precedentes[vecino] = nodo_actual

    return distancia, nodos_precedentes

def obtener_camino(nodos_precedentes, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = nodos_precedentes[actual]
    return camino

def visualizar_grafo(graph, distancia, start):
    G = nx.Graph()
    for nodo, aristas in graph.items():
        for vecino, peso in aristas.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    etiquetas = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas, font_color='red')

    
    for nodo in distancia:
        if distancia[nodo] < float('inf'):
            plt.annotate(f"{distancia[nodo]}", pos[nodo], textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title(f"Grafo con Dijkstra (Inicio: {start})")
    plt.show()


graph = {
   'a': {'b': 7, 'c': 3},
   'b': {'d': 5},
   'c': {'b': 2, 'd': 3, 'e': 6},
   'd': {'f': 5, 'e': 1},
   'e': {'g': 5},
   'g': {'z': 4},
   'f': {'g': 2, 'z': 7},
   'z': {}
}


start_node = "a"
distancia, nodos_precedentes = dijkstra(graph, start_node)

destino = "z"
camino = obtener_camino(nodos_precedentes, destino)
costo = distancia[destino]

print(f"Camino más corto desde {start_node} a {destino}: {camino} con costo: {costo}")

visualizar_grafo(graph, distancia, start_node)



#destino = "z"
#camino = obtener_camino(nodos_precedentes, destino)
#costo = distancia[destino]
#En conjunto, estas líneas de código se utilizan para:
#Establecer el destino al que se quiere llegar ("z").
#btener el camino más corto desde el nodo inicial hasta el destino utilizando la información sobre nodos precedentes.
#Calcular el costo total del camino más corto hasta el nodo de destino
#es una de las funciones que le cambiamos para que nos optimizara nuesto programa


