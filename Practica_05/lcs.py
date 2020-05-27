import numpy as np
import xlsxwriter

class Table:
    def __init__(self, strings):
        #We create the cells according to the size of the strings plus 1
        self.string1 = strings[1]
        self.string2 = strings[0]
        self.columns = len(strings[1]) + 1
        self.rows = len(strings[0]) + 1
        self.cells = np.zeros((self.rows,self.columns,2), dtype=int)

    def set_cell_values(self):
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
                if self.string2[i-1] == self.string1[j-1]:
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
        workbook = xlsxwriter.Workbook('Tabla.xlsx')
        worksheet = workbook.add_worksheet()
        symbols= {-1:'', 0:'🢁', 1:'🢀', 2:'🢄'}
        for i in range(2, self.rows+1):
            worksheet.write(i, 0 , self.string2[i-2])
        for j in range(2, self.columns+1):
            worksheet.write(0, j , self.string1[j-2])
        for i in range(self.rows):
            for j in range(self.columns):
                cell_value = str(self.cells[i][j][0])
                cell_direction =  symbols.get(self.cells[i][j][1])
                worksheet.write(i+1, j+1, cell_value + cell_direction)
        workbook.close()

    def lcs(self):
        i = self.rows-1
        j = self.columns-1
        string_lcs = ''
        length = self.cells[i][j][0]
        while (length):
            direction = self.cells[i][j][1]
            if direction == 2:
                string_lcs = self.string1[j-1] +  string_lcs 
                i, j, length= i-1, j-1, length-1
            elif direction == 1:
                j = j-1
            else: 
                i = i-1
        return string_lcs