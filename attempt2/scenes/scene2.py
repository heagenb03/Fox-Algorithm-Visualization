from manim import VGroup, ORIGIN, LEFT, np
from constants import *
from intial import *

class Scene2:
    def __init__(self):
        self.intial = Intial()
        self.LEFT_ALINGMENT = 1.5
        self.RIGHT_ALINGMENT = 3.6
        
    def createMatrixC(self):
        """Create Matrix C with four entries

        Returns:
            VGroup: Matrix C with two VGroups - one for the number and one for the box
        """
        matrix = VGroup()
        box_list = []
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixFourEntries(MATRIX_A_NUMBERS[entry], MATRIX_B_NUMBERS[entry], 0, 0, MATRIX_A_COLOR, MATRIX_B_COLOR, C_VALUES_COLOR))
            
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix
    
    def moveMatrixCtoCenter(self, matrixB, matrixC):
        """Move Matrix C to center of the screen

        Args:
            matrixB (VGroup): Matrix B from scene 1 (for positioning)
            matrixC (VGroup): Matrix C from scene 2

        Returns:
            list: list of animations that move each VGroup part of Matrix C to the center of the screen
        """
        move_animations = []
        
        for entry in range((MATRIX_ROW_COL_CT**2)):
            #Matrix C
            boxes = matrixC[entry][0]
            box_center = matrixB[entry].get_center()
            target_position = box_center + ORIGIN
            move_animations.append(boxes.animate.move_to(target_position + LEFT * self.LEFT_ALINGMENT))
            
            #Enteries A
            numbers = matrixC[entry][1]
            box_center = matrixB[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * self.LEFT_ALINGMENT))   
                
            #Enteries B
            numbers = matrixC[entry][2]
            box_center = matrixB[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * self.LEFT_ALINGMENT))
            
            #Enteries for moved Aij values
            numbers = matrixC[entry][3]
            box_center = matrixB[entry].get_center()
            offset = np.array([-0.32, -0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * self.LEFT_ALINGMENT))
            
            #Enteries for computed C values
            numbers = matrixC[entry][4]
            box_center = matrixB[entry].get_center()
            offset = np.array([0.32, -0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * self.LEFT_ALINGMENT))
            
        return move_animations