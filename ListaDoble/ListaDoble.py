# Importamos las clases necesarias desde los archivos correspondientes.
from NodoDoble import nodo_doble
from Estudiante import estudiante

# Definimos la clase lista_doble_enlazada.
class lista_doble_enlazada:
    # Constructor de la clase.
    def __init__(self):
        # Inicializamos el primer nodo como None, indicando que la lista está vacía.
        self.primero = None

    # Método para insertar un estudiante en la lista doblemente enlazada.
    def insertar(self, estudiante):
        # Si la lista está vacía, el nuevo estudiante se convierte en el primer nodo.
        if self.primero is None:
            self.primero = nodo_doble(estudiante=estudiante)
            return
        # Si la lista no está vacía, recorremos hasta el último nodo.
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        # Creamos un nuevo nodo con el estudiante y lo enlazamos al último nodo.
        nuevo_nodo = nodo_doble(estudiante=estudiante)
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    # Método para recorrer e imprimir los elementos de la lista doblemente enlazada.
    def recorrer(self):
        # Comenzamos desde el primer nodo.
        actual = self.primero
        # Recorremos la lista mientras haya nodos.
        while actual is not None:
            # Imprimimos los datos del estudiante en el nodo actual.
            print("carne:", actual.estudiante.carne, "nombre:", actual.estudiante.nombre, "email:", actual.estudiante.email, "->")
            # Avanzamos al siguiente nodo.
            actual = actual.siguiente

    # Método para eliminar un estudiante de la lista por su carne.
    def eliminar(self, carne):
        # Comenzamos desde el primer nodo.
        actual = self.primero
        # Buscamos el estudiante con la carne especificada.
        while actual is not None:
            if actual.estudiante.carne == carne:
                # Si encontramos el estudiante, lo eliminamos y ajustamos los enlaces.
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return
            # Avanzamos al siguiente nodo.
            actual = actual.siguiente

    # Método para generar un archivo DOT con la representación de la lista como gráfico Graphviz.
    def generar_graphviz(self, nombre_archivo):
        # Comenzamos desde el primer nodo.
        actual = self.primero
        # Creamos una cadena con el código DOT inicial.
        cadena = "digraph G {\n"
        cadena += "rankdir=LR\n"  # Esto hace que el gráfico sea horizontal
        cadena += "node [shape=box]\n"
        # Recorremos la lista y generamos un nodo en el gráfico para cada estudiante.
        while actual:
            cadena += f'"{actual.estudiante.carne}" [label="{actual.estudiante.carne} - {actual.estudiante.nombre}"]\n'
            # Si hay un siguiente nodo, añadimos una conexión.
            if actual.siguiente:
                cadena += f'"{actual.estudiante.carne}" -> "{actual.siguiente.estudiante.carne}"\n'
            # Si hay un nodo anterior, añadimos una conexión con estilo punteado.
            if actual.anterior:
                cadena += f'"{actual.estudiante.carne}" -> "{actual.anterior.estudiante.carne}"\n'
            # Avanzamos al siguiente nodo.
            actual = actual.siguiente
        # Cerramos el grafo DOT.
        cadena += "}\n"
        # Escribimos la cadena en un archivo con el nombre especificado.
        with open("./" + nombre_archivo, "w") as f:
            f.write(cadena)
