from manim import Rectangle, VGroup, Text, DOWN, RIGHT, UL, UR, LEFT
from constants import *

#Intialize functions utilized in the scenes
class Intial:
    #Creates the individual "box" within a matrix
    def createMatrixBox(self):
        matrix_box = Rectangle(
                height=1,
                width=1,
                fill_color=MATRIX_BG_COLOR,
                fill_opacity=0.7,
                stroke_color=MATRIX_BORDER_COLOR
            )
        
        return matrix_box

    #Intializes the "box" as empty
    def createBlankMatrixEntries(self):
        result = VGroup()
        
        result.add(self.createMatrixBox())
        
        return result

    #Intailizes a "box" with one entry
    def createMatrixEntry(self, num, txt_color):
        result = VGroup()
        
        entry = Text(str(num), font_size=MATRIX_FONT_SIZE, color=txt_color, fill_opacity=0.9)
        result.add(self.createMatrixBox(), entry)
        
        return result

    #Intailize a "box" with two enteries
    def createTwoMatrixEntries(self, first_num, second_num, first_txt_color, second_txt_color):
        DOWN_ALINGMENT = 0.1
        RIGHT_ALINGMENT = 0.1
        result = VGroup()
        matrix_box = self.createMatrixBox()
        
        first_entry = Text(str(first_num), font_size=MATRIX_FONT_SIZE, color=first_txt_color, fill_opacity=0.9)
        second_entry = Text(str(second_num), font_size=MATRIX_FONT_SIZE, color=second_txt_color, fill_opacity=0.9)
        first_entry.align_to(matrix_box, UL).shift(DOWN * DOWN_ALINGMENT + RIGHT * RIGHT_ALINGMENT)
        second_entry.align_to(matrix_box, UR).shift(DOWN * DOWN_ALINGMENT + LEFT * RIGHT_ALINGMENT)
        
        result.add(matrix_box, first_entry, second_entry)
        
        return result

    #Creates a copy of the entries in the matrix to be used for animations
    def createMatrixCopy(self, matrix):
        matrixA_copy = []
        matrixB_copy = []
        
        for column in range(MATRIX_ROW_COL_CT - 1):
            for box in range(MATRIX_ROW_COL_CT**2):
                matrixA_copy.append(matrix[box][1].copy())
                
        for box in range(MATRIX_ROW_COL_CT**2):
            matrixB_copy.append(matrix[box][2].copy())
                
        return matrixA_copy, matrixB_copy
                