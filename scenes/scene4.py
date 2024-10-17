from manim import Text, MathTex, FadeIn, FadeOut, ArcBetweenPoints, MoveAlongPath, RIGHT, DR, LEFT, UP, DOWN, ORIGIN, PI, np
from constants import *

#Scene 4
class Scene4:
    def __init__(self):
        self.RIGHT_ALINGMENT = 0.35
        self.LEFT_ALINGMENT = 0.3
        self.UP_ALINGMENT = 0.28
    
    #Updates the values of the matrix C by the product of the values of matrix A(i) and B values to create C values
    def updateABValuesToC(self, matrix):
        fade_in_animations = []    
        fade_out_animations = []
        
        for box in range(len(matrix)):
            entry_a = int(matrix[box][3].text)
            entry_b = int(matrix[box][2].text)
            
            print(f'Entry A: {entry_a} Entry B: {entry_b}')
            value_c = entry_a * entry_b
            
            multi_sign = MathTex("\\times", font_size = 30)
            multi_sign.move_to(matrix[box][1].get_center()).shift(DOWN * self.UP_ALINGMENT + RIGHT * self.RIGHT_ALINGMENT)
            
            entry_c = Text(str(value_c + int(matrix[box][4].text)), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR)
    
            matrix[box].add(multi_sign)
            
            fade_in_animations.append(FadeIn(multi_sign))
            fade_in_animations.append(matrix[box][4].animate.become(entry_c).move_to(matrix[box][4].get_center()))
            
            fade_out_animations.append(FadeOut(multi_sign))
    
        return fade_in_animations, fade_out_animations

    def moveBvalues(self, shift_count, matrix):
        move_animations = []
        
        if shift_count != 0:
            for row in range(MATRIX_ROW_COL_CT):
                #First Row
                if row == 0:
                    for col in range(MATRIX_ROW_COL_CT):
                        intial_entry = col
                        final_point_entry = col + (MATRIX_ROW_COL_CT * 2)
                        
                        arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center() + ORIGIN, angle=PI/2)
                        move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
                        
                #Middle Rows & Final Row
                else:
                    for col in range(MATRIX_ROW_COL_CT):
                        intial_entry = (col + (row * MATRIX_ROW_COL_CT))
                        final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
                        
                        arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center() + ORIGIN, angle=PI/2)
                        move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
        
        return move_animations, matrix