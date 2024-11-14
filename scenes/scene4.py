from manim import FadeOut, RIGHT, VGroup
from constants import *
from intial import Intial
from scene3 import Scene3

class Scene4:
    def __init__(self):
        self.intial = Intial()
        self.scene3 = Scene3()
        
    def fadeOutEntries(self, matrix):
        fade_out_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            fade_out_animations.append(FadeOut(matrix[entry][MATRIX_C_ENTRY_A_VGROUP]))
            fade_out_animations.append(FadeOut(matrix[entry][MATRIX_C_ENTRY_B_VGROUP]))
            
        return fade_out_animations
    
    def moveCEnteriesToCenter(self, matrix):
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP]
            move_animations.append(numbers.animate.move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center()))
            
        return move_animations
    
    def moveMatrixCtoOriginalPosition(self, matrixPos, matrixC):
        alingmnet = RIGHT * 0.15
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            #Matrix C
            boxes = matrixC[entry][MATRIX_C_BOX_VGROUP]
            move_animations.append(boxes.animate.move_to(self.intial.getTargetPosition(matrixPos, entry, MATRIX_C_BOX_VGROUP) + alingmnet))
            
            #Enteries C
            numbers = matrixC[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixPos, entry, MATRIX_C_BOX_VGROUP) + alingmnet))   
                
        return move_animations