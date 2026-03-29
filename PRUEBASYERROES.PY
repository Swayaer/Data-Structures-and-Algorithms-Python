import matplotlib.pyplot as plt



class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato


def insertar (raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                    insertar(raiz.izquierda, nodo)



def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)
def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        inorden(raiz.izquierda)
        inorden(raiz.derecha)

def postorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        inorden(raiz.derecha)
        print(raiz.dato)

idato =int(input("ingrese un numero"))

raiz = Nodo(idato)

idato =int(input("ingrese un numero"))

insertar(raiz, Nodo(idato))

idato =int(input("ingrese un numero"))
insertar(raiz, Nodo(idato))
idato = int(input("ingrese un numero"))
insertar(raiz, Nodo(idato))
idato = int(input("ingrese un numero"))
insertar(raiz, Nodo(idato))
idato = int(input("ingrese un numero"))
insertar(raiz, Nodo(idato))




inorden(raiz)

print()

preorden(raiz)

print()

postorden(raiz)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

def plot_tree(node, x, y, dx):
    if node is not None:
        plt.text(x, y, str(node.value), ha='center', va='center', bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='lightblue'))
        if node.left:
            plt.plot([x, x - dx], [y - 0.1, y - 0.5], 'k-')
            plot_tree(node.left, x - dx, y - 0.5, dx / 2)
        if node.right:
            plt.plot([x, x + dx], [y - 0.1, y - 0.5], 'k-')
            plot_tree(node.right, x + dx, y - 0.5, dx / 2)

def draw_tree(tree):
    plt.figure(figsize=(10, 6))
    plt.title('Árbol Binario de Búsqueda')
    plot_tree(tree.root, 0, 0, 4)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    
    bst = BinaryTree()
    

    valores = [9,3,4,7,8,6,5,2,1]
    for val in valores:
        bst.insert(val)

    draw_tree(bst)



    #Este codigo es la prime version extraida de un video de youtube donde realizan el inorden, preorden , postorden de los nodos de un arbol grafico pero como podemos 
    # ver esta muy revuelto y pide individualmente los nodos para realizar la accion y luego dibujar el arbol y nuestro arbol habioa que ingresar los valores como tal
    # siendo poco eficiente y tardado la aplicacion de matplotlib para dibujar este arbol por asi decirlo surgio a base de videos y documentacion encontrada en internet  


import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = []  # Inicializa vecinos como una lista vacía
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregar_vecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])  # Almacena vecinos como [vecino, peso]

class Grafica:
    def __init__(self):
        self.G = nx.Graph()
        self.vertices = {}  # Usa un diccionario para almacenar los vértices por id

    def mostrar_grafica(self):
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()

    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)  # Agrega un nuevo vértice al diccionario

    def agregar_arista(self, vertice_a, vertice_b, peso):
        if vertice_a in self.vertices and vertice_b in self.vertices:
            self.vertices[vertice_a].agregar_vecino(vertice_b, peso)
            self.vertices[vertice_b].agregar_vecino(vertice_a, peso)
            self.G.add_edge(vertice_a, vertice_b, weight=peso)  # Corrigió 'weigth' a 'weight'

    def obtener_camino(self, vertice_b):
        camino = []  # Inicializa el camino
        actual = vertice_b
        while actual is not None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[vertice_b].distancia]

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v
        return None  # Agregada la devolución para el caso de lista vacía

    def dijkstra(self, vertice_a):
        if vertice_a in self.vertices:
            self.vertices[vertice_a].distancia = 0
            actual = vertice_a
            no_visitados = []
            # Se agregan todos a no visitados
            for v in self.vertices:
                if v != vertice_a:
                    self.vertices[v].distancia = float('inf')
                    self.vertices[v].padre = None
                no_visitados.append(v)
                
            while len(no_visitados) > 0:
                # Se evaluan los vertices vecinos y se toma el menor
                for vecino in self.vertices[actual].vecinos:
                    if not self.vertices[vecino[0]].visitado:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                
                self.vertices[actual].visitado = True
                no_visitados.remove(actual)
                
                if len(no_visitados) > 0:
                    actual = self.minimo(no_visitados)
                else:
                    break  # Sale si no hay más vértices no visitados
        else:
            return False

if __name__ == '__main__':
    gr = Grafica()
    gr.agregar_vertice('a')
    gr.agregar_vertice('b')
    gr.agregar_vertice('c')
    gr.agregar_vertice('d')
    gr.agregar_vertice('e')
    gr.agregar_vertice('f')
    gr.agregar_vertice('g')
    gr.agregar_vertice('h')
    gr.agregar_vertice('i')
    gr.agregar_vertice('j')
    gr.agregar_vertice('k')
    gr.agregar_vertice('l')  # Corregido de '1' a 'l' para que sea un identificador válido
    gr.agregar_vertice('m')
    gr.agregar_vertice('n')
    gr.agregar_vertice('p')
    
    gr.agregar_arista('a', 'b', 8)
    gr.agregar_arista('a', 'e', 4)
    gr.agregar_arista('a', 'd', 5)
    gr.agregar_arista('b', 'e', 12)
    gr.agregar_arista('b', 'f', 4)
    gr.agregar_arista('b', 'c', 3)
    gr.agregar_arista('c', 'f', 9)
    gr.agregar_arista('c', 'g', 11)
    gr.agregar_arista('d', 'e', 9)
    gr.agregar_arista('d', 'h', 6)
    gr.agregar_arista('e', 'f', 3)
    gr.agregar_arista('e', 'i', 8)
    gr.agregar_arista('e', 'j', 5)
    gr.agregar_arista('f', 'g', 1)
    gr.agregar_arista('f', 'k', 8)
    gr.agregar_arista('g', 'k', 8)
    gr.agregar_arista('g', 'l', 7)  # Corregido de '1' a 'l'
    gr.agregar_arista('h', 'i', 2)
    gr.agregar_arista('h', 'm', 7)
    gr.agregar_arista('i', 'm', 6)
    gr.agregar_arista('i', 'j', 10)
    gr.agregar_arista('j', 'n', 9)
    gr.agregar_arista('j', 'k', 6)
    gr.agregar_arista('k', 'l', 5)  # Corregido de '1' a 'l'
    gr.agregar_arista('k', 'p', 7)
    gr.agregar_arista('l', 'p', 6)  # Corregido de '1' a 'l'
    gr.agregar_arista('m', 'n', 2)
    gr.agregar_arista('n', 'p', 12)
    
    print("La ruta más rápida por Dijkstra es:")
    gr.dijkstra('a')
    print(gr.obtener_camino('p'))
    gr.mostrar_grafica()  # Corregido de 'gr.mostrarg' a 'gr.mostrar_grafica'

#ste codigo es recopilado talcual de un proyecto de unos estudinates en youtube sobre este recorrido pero al igual que el otro es poco eficiente ya que podemos ver que hay que ingresar manualmente raiz y aeistas 
#muchas veces y la diferencia es que este no nos mostraba la ruta mas corta y el coste como tal 



