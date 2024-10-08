from manim import VGroup, np
from constants import *
from intial import Intial

#Scene 1
class Scene1:
    def __init__(self):
        self.intial = Intial()
        
    #Creates Matrix A with "boxes" with enteries
    def createMatrixA(self):
        box_list = []
        matrix = VGroup()
         
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixEntry(MATRIX_A_NUMBERS[entry], MATRIX_A_COLOR))
        
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        
        return matrix

    #Creates Matrix B with "boxes" with enteries
    def createMatrixB(self):
        box_list = []
        matrix = VGroup()
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixEntry(MATRIX_B_NUMBERS[entry], MATRIX_B_COLOR))
        
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        
        return matrix

    #Creates a Matrix C with blank "boxes"
    def createMatrixC(self):
        box_list = []
        matrix = VGroup()
        
        for box in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createBlankMatrixEntries())
        matrix.add(*box_list)
        
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix
    
    def moveEnteriesToMatrixC(self, matrixA, matrixB, matrixC):
        move_animations = []
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrixA[entry][1]
            box_center = matrixC[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            move_animations.append(numbers.animate.move_to(target_position)) 
            
            numbers = matrixB[entry][1]
            box_center = matrixC[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            move_animations.append(numbers.animate.move_to(target_position)) 
        
        return move_animations