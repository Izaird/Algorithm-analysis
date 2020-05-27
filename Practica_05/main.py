from lcs import *

def get_strings(file_name):
    while True:
        try:
            file = open(file_name, "r")
            strings = (file.read().split("\n\n"))
            return strings
        except FileNotFoundError:
            filem_name = input("Archivo no existe intente de nuevo:")
            
class State:
    def __init__(self):
        self._value = 0
        self._direction = -1

    @property
    def value(self):
        return self._value

    #chahdahsdfklj
    @value.setter
    def value(self, value):
        self._value = value


    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction


if __name__ == "__main__":

    # file_name = input("Nombre del archivo que desea analizar:")
    strings = get_strings("04")
    print(len(strings))
    table = Table(strings)
    table.set_cell_values()
    table.print_cells()
    print("AY LMAO")