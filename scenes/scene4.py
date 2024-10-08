from manim import Text, MathTex, FadeIn, FadeOut, ArcBetweenPoints, MoveAlongPath, RIGHT, DR, LEFT, UP, ORIGIN, PI
from constants import *

#Scene 4
class Scene4:
    def __init__(self):
        self.RIGHT_ALINGMENT = 0.45
        self.LEFT_ALINGMENT = 0.3
        self.UP_ALINGMENT = 0.1
    
    #Updates the values of the matrix C by the product of the values of matrix A(i) and B values to create C values
    def updateABValuesToC(self, matrix):
        fade_in_animations = []    
        fade_out_animations = []
        
        col = 0
        row = 0
        for box in matrix:
            entry_a = int(box[1].text)
            entry_b = int(box[2].text)
            
            value_c = entry_a * entry_b
            
            multi_sign = MathTex("\\times", font_size = 20)
            
            multi_sign.move_to(box[1].get_center()).shift(RIGHT * self.RIGHT_ALINGMENT)
            
            entry_c = Text(str(value_c), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR)
            entry_c.align_to(box[0], DR).shift(UP * self.UP_ALINGMENT + LEFT * self.LEFT_ALINGMENT)
            
            box.add(multi_sign, entry_c)
            
            fade_in_animations.append(FadeIn(multi_sign))
            fade_in_animations.append(FadeIn(entry_c))
            
            fade_out_animations.append(FadeOut(multi_sign))
            fade_out_animations.append(FadeOut(entry_c))
    
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