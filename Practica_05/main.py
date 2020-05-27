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
    
class Table:
    def __init__(self, strings):
        #We create the cells according to the size of the strings plus 1
        self.strings = strings
        self.number_of_columns = len(strings[0]) + 1
        self.number_of_rows = len(strings[1]) + 1
        self.cells = [[None for _ in range(self.number_of_columns)] for _ in range(self.number_of_rows)]



    def set_cell_values(self):
        string1 = strings[0]
        string2 = strings[1]
        #I first fill the first column and the first row with states that have the value of 1 and without an direction
        for column in range(self.number_of_columns):
            self.cells[0][column] = State()
        for row in range(1,self.number_of_rows):
            self.cells[row][0] = State()

        #Then I continue with the rest of the cells 
        for i in range(1,self.number_of_rows):
            for j in range(1,self.number_of_columns):
                #We compare the strings with each other
                self.cells[i][j] = State()
                if string2[i-1] == string1[j-1]:
                    self.cells[i][j].direction = 2 #diagonal
                    self.cells[i][j].value = self.cells[i-1][j-1].value + 1 

                elif self.cells[i-1][j].value <= self.cells[i][j-1].value:
                    self.cells[i][j].direction = 1 #left
                    self.cells[i][j].value = self.cells[i][j-1].value

                else:
                    self.cells[i][j].direction = 0 #up
                    self.cells[i][j].value = self.cells[i-1][j].value
        
    
    def print_cells(self):
        pass

if __name__ == "__main__":

    # file_name = input("Nombre del archivo que desea analizar:")
    strings = get_strings("04")
    print(len(strings))
    table = Table(strings)
    table.set_cell_values()
    # table.print_cells()
    print("AY LMAO")