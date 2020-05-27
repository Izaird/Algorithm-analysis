from lcs import *

def get_strings(file_name):
    while True:
        try:
            file = open(file_name, "r")
            strings = (file.read().split("\n\n"))
            return strings
        except FileNotFoundError:
            filem_name = input("Archivo no existe intente de nuevo:")

if __name__ == "__main__":

    file_name = input("Nombre del archivo que desea analizar:")
    strings = get_strings(file_name)
    table = Table(strings)
    table.set_cell_values()
    # table.print_cells()
    lcs = table.lcs()
    print("lcs = " + lcs)
    print(len(lcs))