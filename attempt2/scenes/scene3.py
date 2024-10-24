from manim import ArcBetweenPoints, MoveAlongPath, PI, RIGHT, Text
from constants import *
from intial import *

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.LEFT_ALINGMENT = 1.5
        self.DOWN_ALINGMENT = 0.3
        self.moved_aij_values = []
        
    def moveEnteriesAcrossRight(self, matrix, entry):
        move_animations = []
        for column in range(MATRIX_ROW_COL_CT - 1):
            final_point_entry = entry + column + 1

            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy(), arcPath))
            
        self.moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text())
            
        return move_animations
    
    def moveEnteriesAcrossLeft(self, matrix, entry):
        move_animations = []
        for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
            final_point_entry = entry - column
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy(), arcPath))
            
        self.moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text())
            
        return move_animations
    
    def moveEnteriesAcrossRightAndLeft(self, matrix, entry, column):
        move_animations = []
        
        #Columns behind intial position
        for back_column in range((MATRIX_ROW_COL_CT - 1) - column):
            final_point_entry = entry - back_column - 1
                
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy(), arcPath))
        
        #Columns in front of intial position
        for front_column in range((MATRIX_ROW_COL_CT - 1) - column):
            final_point_entry = entry + front_column + 1
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy(), arcPath))
        
        self.moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text())
        
        return move_animations
    
    def updateComputedCValues(self, matrix):
        for box in range(MATRIX_ROW_COL_CT):
            entry_a = int(matrix[box][MATRIX_C_ENTRY_A_VGROUP].get_text())
            entry_b = int(matrix[box][MATRIX_C_ENTRY_B_VGROUP].get_text())
            
            value_c = entry_a * entry_b
            matrix[box][MATRIX_C_ENTRY_COMPUTED_C_VGROUP].set_text(str(value_c))