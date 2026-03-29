import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato

def insertar(raiz, nodo):
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
        print(raiz.dato, end=' ')
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz is not None:
        print(raiz.dato, end=' ')
        preorden(raiz.izquierda)
        preorden(raiz.derecha)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato, end=' ')

def plot_tree(node, x, y, dx):
    if node is not None:
        plt.text(x, y, str(node.dato), ha='center', va='center', 
                 bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='lightblue'))
        if node.izquierda:
            plt.plot([x, x - dx], [y - 0.1, y - 0.5], 'k-')
            plot_tree(node.izquierda, x - dx, y - 0.5, dx / 2)
        if node.derecha:
            plt.plot([x, x + dx], [y - 0.1, y - 0.5], 'k-')
            plot_tree(node.derecha, x + dx, y - 0.5, dx / 2)

def draw_tree(raiz):
    plt.figure(figsize=(10, 6))
    plt.title('Árbol Binario de Búsqueda')
    plot_tree(raiz, 0, 0, 4)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    raiz = None

    valores = [int(x) for x in input("Ingrese números separados por espacios: ").split()]

    for val in valores:
        if raiz is None:
            raiz = Nodo(val)
        else:
            insertar(raiz, Nodo(val))

    
    print("Recorrido inorden:")
    inorden(raiz)
    print("\nRecorrido preorden:")
    preorden(raiz)
    print("\nRecorrido postorden:")
    postorden(raiz)

   
    draw_tree(raiz)

#esta es la version que pudimos mejorar notoriamente la eficacia y rapidez a comparacion de nuestro primer codigo el cual era tosco desordenado y no estab unificaco 
#por lo cual era dificil de leer y entender a hora este de aca las mejoras realizadas fueron sustituir idato =int(input("ingrese un numero"))
#raiz = Nodo(idato)
#idato =int(input("ingrese un numero"))
#insertar(raiz, Nodo(idato))
#idato =int(input("ingrese un numero"))
#insertar(raiz, Nodo(idato))
#idato = int(input("ingrese un numero"))
#insertar(raiz, Nodo(idato))
#idato = int(input("ingrese un numero"))
#insertar(raiz, Nodo(idato))
#idato = int(input("ingrese un numero"))
#insertar(raiz, Nodo(idato))
#que eran las maneras poco eficientes de pedir los nodos y realiar los procesos a hora veremos 
# for val in valores:
 #       if raiz is None:
  #          raiz = Nodo(val)
    #    else:
       #     insertar(raiz, Nodo(val))Este comando muestra un mensaje al usuario pidiéndole que ingrese varios números en una sola línea, separados por espacios. Por ejemplo, si el usuario ingresa 1 2 3 4 5 8
       # esta entrada se almacenara en una cadena de texto 
       
#el método split() se aplica a la cadena de entrada. Este método divide la cadena en una lista de subcadenas, utilizando los espacios como separadores. Con la entrada 5 3 8 1 4, el resultado sería la lista ['5', '3', '8', '1', '4'
#En resumen, este bloque de código permite al usuario ingresar una serie de números en una sola línea, separarlos en una lista de enteros y luego construir un árbol logico.






