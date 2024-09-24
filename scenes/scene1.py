from manim import VGroup
from constants import *
from intial import *

#Scene 1

#Creates Matrix A with "boxes" with enteries
def createMatrixAScene1():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_A_NUMBERS[entry], MATRIX_A_COLOR))
    
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates Matrix B with "boxes" with enteries
def createMatrixBScene1():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_B_NUMBERS[entry], MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates a Matrix C with blank "boxes"
def createMatrixCScene1():
    matrix = VGroup()
    box_list = []
    
    for box in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createBlankMatrixEntries())
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    return matrix