from lcs import *
import time
def get_strings(file_name):
    while True:
        try:
            file = open(file_name, "r")
            strings = (file.read().split("\n\n"))
            return strings
        except FileNotFoundError:
            file_name = input("Archivo no existe intente de nuevo:")

if __name__ == "__main__":

    file_name = input("Nombre del archivo que desea analizar:")
    start = time.time()
    strings = get_strings(file_name)
    table = Table(strings)
    table.set_cell_values()
    lcs = table.lcs()
    end = time.time()
    print("lcs = " + lcs)
    print(len(lcs))
    print(end - start)
    similarity_percentage  = (len(lcs)*100)/len(strings[0])
    print("%.2f" % similarity_percentage + '%')
    #I do not measure the time it takes to create the file that stores the table because it is not a necessary process to calculate lcs
    table.print_cells()