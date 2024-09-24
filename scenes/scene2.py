from manim import VGroup
from constants import *
from intial import *


#Scene 2

#Create Matrix C with numbers from Matrix A & C
def createMatrixCScene2():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createTwoMatrixEntries(MATRIX_A_NUMBERS[entry], MATRIX_B_NUMBERS[entry], MATRIX_A_COLOR, MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    return matrix