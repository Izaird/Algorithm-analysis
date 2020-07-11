class Nodo(object):

    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def __repr__(self):
        return self.nombre   


def leer_archivo(nombre_archivo):
    nodos = []
    nodos_vecinos = []
    i = 0
    lineas = ([line.split() for line in open(nombre_archivo)])
    for linea in lineas:
        nodos.append(Nodo(linea[0]))
    
    for linea in lineas:
        nodos_vecinos = linea[1:]
        for nodo_vecino in nodos_vecinos:
            nodo = next((x for x in nodos if x.nombre == nodo_vecino), None)
            nodos[i].vecinos.append(nodo)
        i += 1

    return nodos


def encontrar_cliques(potencial_clique=[], nodos_restantes=[], saltar_nodo=[], profundidad=0):

    if len(nodos_restantes) == 0 and len(saltar_nodo) == 0:
        print('Este es un clique:', potencial_clique)
        return 1

    found_cliques = 0
    for nodo in nodos_restantes:

        #Intentamos añadir un nodo al potencial_clique para ver si podemos hacer que funcione.
        nuevo_potencial_clique = potencial_clique + [nodo]
        nuevos_nodos_restantes = [n for n in nodos_restantes if n in nodo.vecinos]
        nuevos_saltar_nodo = [n for n in saltar_nodo if n in nodo.vecinos]
        found_cliques += encontrar_cliques(nuevo_potencial_clique, nuevos_nodos_restantes, nuevos_saltar_nodo, profundidad + 1)

        """Terminamos de considerar este nodo.  Si hubiera una forma de formar un clique con el, ya 
        hemos descubierto su maximo clique en la llamada recursiva de arriba.  Entonces se puede agregar
        y eliminar de los nodos restantes y se agrega a la lista de saltar nodo."""
        nodos_restantes.remove(nodo)
        saltar_nodo.append(nodo)
    return found_cliques



nodos = leer_archivo("02")
total_cliques = encontrar_cliques(nodos_restantes=nodos)
print('Numero de cliques encontrados:', total_cliques)
