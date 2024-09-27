from manim import Text, MathTex, FadeIn, FadeOut, ArcBetweenPoints, MoveAlongPath, RIGHT, DR, LEFT, UP, ORIGIN, PI
from constants import *

#Updates the values of the matrix C by the product of the values of matrix A(i) and B values to create C values
def updateABValuesToC(matrix, matrix_aj_values):
    RIGHT_ALINGMENT = 0.45
    LEFT_ALINGMENT = 0.3
    UP_ALINGMENT = 0.1
    
    fade_in_animations = []
    fade_out_animations = []
    
    col = 0
    row = 0
    for box in matrix:
        entry_a = int(matrix[MATRIX_ROW_COL_CT * row + row][1].text)
        entry_b = int(box[2].text)
        value_c = entry_a * entry_b
        
        multi_sign = MathTex("\\times", font_size = 20)
        
        multi_sign.move_to(box[1].get_center()).shift(RIGHT * RIGHT_ALINGMENT)
        
        entry_c = Text(str(value_c), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR)
        entry_c.align_to(box[0], DR).shift(UP * UP_ALINGMENT + LEFT * LEFT_ALINGMENT)
        
        box.add(multi_sign, entry_c)
        
        fade_in_animations.append(FadeIn(multi_sign))
        fade_in_animations.append(FadeIn(entry_c))
        
        fade_out_animations.append(FadeOut(multi_sign))
        
        #Entry Aij values
        for entry in matrix_aj_values:
            fade_out_animations.append(FadeOut(entry))
            
        fade_out_animations.append(FadeOut(entry_c, scale=0.5))
        
        if col == MATRIX_ROW_COL_CT - 1:
            col = 0
            row += 1
        else:
            col += 1
            
    return fade_in_animations, fade_out_animations

def moveBvalues(shift_count, matrix_copy, matrix):
    move_animations = []
    fade_out_animations = []
    if shift_count != 0:
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = col
                    final_point_entry = col + (MATRIX_ROW_COL_CT * 2)
                    
                    arcPath = ArcBetweenPoints(matrix_copy[intial_entry].get_center(), matrix_copy[final_point_entry].get_center() + ORIGIN, angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix_copy[intial_entry], arcPath))
                    
            #Middle Rows & Final Row
            else:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = (col + (row * MATRIX_ROW_COL_CT))
                    final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
                    
                    arcPath = ArcBetweenPoints(matrix_copy[intial_entry].get_center(), matrix_copy[final_point_entry].get_center() + ORIGIN, angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix_copy[intial_entry], arcPath))
            
            #Fade out Previous MatrixBij values
            for entry in range(MATRIX_ROW_COL_CT**2):
                fade_out_animations.append(FadeOut(matrix[entry][2]))
    
    return move_animations, fade_out_animations