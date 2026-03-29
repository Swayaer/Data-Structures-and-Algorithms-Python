Este repositorio contiene la implementación, visualización y optimización de estructuras de datos fundamentales desarrolladas para el curso de Matemática Discreta.

Lenguaje: Python 3

Visualización: Matplotlib
Lógica de Grafos: NetworkX

Árboles Binarios de Búsqueda (BST)
En esta sección se implementó la lógica de nodos para realizar recorridos sistemáticos y una representación gráfica del árbol.
Mejoras de Eficiencia:
Optimización de Entrada: Se sustituyó la petición manual de nodos uno por uno por un método dinámico utilizando .split().
Procesamiento: Ahora el usuario puede ingresar una serie de números en una sola línea, los cuales se convierten automáticamente en una lista de enteros para construir el árbol de forma masiva.
Recorridos: Implementación completa de Inorden, Preorden y Postorden.
Algoritmo de Dijkstra (Grafos)
Implementación del algoritmo de caminos mínimos para encontrar la ruta más corta entre dos nodos en un grafo ponderado.
Características Principales:
Cálculo de Costo: El programa no solo visualiza el grafo, sino que calcula y muestra el costo total del camino hacia el destino.
Automatización: A diferencia de versiones anteriores donde las aristas se ingresaban manualmente de forma repetitiva, esta versión optimiza la búsqueda de nodos precedentes para reconstruir la ruta exacta.
Visualización: Generación de grafos dinámicos con etiquetas de peso en las aristas.

Cómo ejecutarlo
Clona el repositorio: git clone https://github.com/Swayaer/Data-Structures-and-Algorithms-Python.git

Instala las dependencias necesarias:

**pip install matplotlib networkx**

Ejecuta cualquiera de los archivos .py para ver la lógica y la gráfica resultante.
