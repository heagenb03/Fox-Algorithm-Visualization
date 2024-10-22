from manim import ArcBetweenPoints, MoveAlongPath, PI, RIGHT, Text
from constants import *
from intial import *

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.LEFT_ALINGMENT = 1.5
        self.DOWN_ALINGMENT = 0.3
    
    def moveEnteriesAcrossRight(self, matrix, entry):
        move_animations = []
        for column in range(MATRIX_ROW_COL_CT - 1):
            final_point_entry = entry + column + 1

            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy(), arcPath))
            
        return move_animations
    
    def updateMatrixC(self, matrixC):
        matrix = matrixC.copy()
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            entry3 = MATRIX_A_NUMBERS[entry]
            entry4 = entry3 * MATRIX_B_NUMBERS[entry]
            
            matrix[entry][3] = Text(str(entry3), font_size=MATRIX_FONT_SIZE, color=MATRIX_A_COLOR, fill_opacity=MATRIX_TEXT_OPACITY).move_to(self.intial.getTargetPosition(matrixC, entry, 3) + LEFT * self.LEFT_ALINGMENT)
            matrix[entry][4] = Text(str(entry4), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR, fill_opacity=MATRIX_TEXT_OPACITY).move_to(self.intial.getTargetPosition(matrixC, entry, 4) + LEFT * self.LEFT_ALINGMENT)
        
        return matrix
        