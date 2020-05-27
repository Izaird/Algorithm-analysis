import numpy as np
import xlwt

class Table:
    def __init__(self, strings):
        #We create the cells according to the size of the strings plus 1
        self.strings = strings
        self.columns = len(strings[0]) + 1
        self.rows = len(strings[1]) + 1
        self.cells = np.zeros((self.rows,self.columns,2), dtype=int)



    def set_cell_values(self):
        string1 = self.strings[0]
        string2 = self.strings[1]
        #I first fill the first column and the first row with states that have the value of 1 and without an direction
        for column in range(self.columns):
            self.cells[0][column][0] ,  self.cells[0][column][1] = 0, -1
        for row in range(1,self.rows):
            self.cells[row][0][0] ,  self.cells[row][0][1] = 0, -1


        #Then I continue with the rest of the cells 
        for i in range(1,self.rows):
            for j in range(1,self.columns):
                left_cell =self.cells[i][j-1][0]
                top_cell = self.cells[i-1][j][0]
                #We compare the strings with each other
                if string1[i-1] == string2[j-1]:
                    self.cells[i][j][0] = self.cells[i-1][j-1][0] + 1 
                    self.cells[i][j][1] = 2 #diagonal direction

                #If the simbols are different then we compare wich value is greater betwen the upper cell and the left cell
                elif top_cell > left_cell:
                    self.cells[i][j][0] = top_cell
                    self.cells[i][j][1] = 0 #up direction

                else:
                    self.cells[i][j][0] = left_cell
                    self.cells[i][j][1] = 1 #left direction
        
    
    def print_cells(self):
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1")
        symbols= {-1:'', 0:'🢁', 1:'🢀', 2:'🢄'}
        for i in range(self.rows):
            for j in range(self.columns):
                cell_value = str(self.cells[i][j][0])
                cell_direction =  symbols.get(self.cells[i][j][1])
                sheet1.write(i, j, cell_value + cell_direction)

        book.save("trial.xls")
