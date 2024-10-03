from manim import VGroup, ORIGIN, LEFT, np
from constants import *
from intial import *

#Scene 2
class Scene2:
    def __init__(self):
        self.intial = Intial()
    
    #Create Matrix C with numbers from Matrix A & C
    def createMatrixC(self):
        matrix = VGroup()
        box_list = []
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createTwoMatrixEntries(MATRIX_A_NUMBERS[entry], MATRIX_B_NUMBERS[entry], MATRIX_A_COLOR, MATRIX_B_COLOR))
            
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix
    
    def moveMatrixCtoCenter(self, matrixB, matrixC, alingment):
        move_animations = []
        
        for entry in range((MATRIX_ROW_COL_CT**2)):
            #Matrix C
            boxes = matrixC[entry][0]
            box_center = matrixB[entry].get_center()
            target_position = box_center + ORIGIN
            move_animations.append(boxes.animate.move_to(target_position + LEFT * alingment))
            
            #Enteries A
            numbers = matrixC[entry][1]
            box_center = matrixB[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * alingment))   
                
            #Enteries B
            numbers = matrixC[entry][2]
            box_center = matrixB[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * alingment))
            
        return move_animations