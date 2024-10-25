from manim import ArcBetweenPoints, MoveAlongPath, MathTex, FadeOut, FadeIn, PI, RIGHT, DR, UP, Text, Transform
import numpy as np
from constants import *
from intial import *

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.LEFT_ALINGMENT = 1.5
        self.DOWN_ALINGMENT = 0.3
        self.moved_aij_values = np.array([])
        self.computed_c_values = self.intial.returnComputedCAsArray()
        self.temp_computed_c_values = self.intial.returnComputedCAsArray()
        self.entry_b_values = np.array([MATRIX_B_NUMBERS])
    
    def moveBvalues(self, matrix):
        move_animations = []
        
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = col
                    final_point_entry = col + (MATRIX_ROW_COL_CT * 2)
                    
                    arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center() + ORIGIN, angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
                    
                    self.entry_b_values.append(int(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_text()))
                    
            #Middle Rows & Final Row
            else:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = (col + (row * MATRIX_ROW_COL_CT))
                    final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
                    
                    arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center() + ORIGIN, angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
                    
                    self.entry_b_values.append(int(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_text()))
        
        return move_animations
    
    def moveEnteriesAcrossRight(self, matrix, entry):
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        count = 0
        for column in range(MATRIX_ROW_COL_CT - 1):
            final_point_entry = entry + column + 1
            temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count], shift=UP))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

        return move_animations, fade_out_animations
    
    def moveEnteriesAcrossLeft(self, matrix, entry):
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        count = 0
        for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
            final_point_entry = entry - column
            temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count], shift=UP))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))
        
        return move_animations, fade_out_animations
    
    def moveEnteriesAcrossRightAndLeft(self, matrix, entry, row):
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        for value in range(MATRIX_ROW_COL_CT - 1):
            temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
        
        #Columns behind intial position
        count = 0
        for back_column in range(row):
            final_point_entry = entry - back_column - 1
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count], shift=UP))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        #Columns in front of intial position
        for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
            final_point_entry = entry + front_column + 1
        
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
        
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count], shift=UP))
        
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))
        
        return move_animations, fade_out_animations
    
    def updateComputedCValues(self, matrix):
        self.temp_computed_c_values = self.moved_aij_values * self.entry_b_values
        self.computed_c_values += self.temp_computed_c_values
        
        transform_animations = []
        fade_in_animations = []
        fade_out_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            c_value = Text(str(self.computed_c_values[entry]), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR, fill_opacity=MATRIX_TEXT_OPACITY)
            c_value.align_to(self.intial.getTargetPosition(matrix, entry, MATRIX_C_ENTRY_COMPUTED_C_VGROUP), DR).shift(DOWN * 0.11 + RIGHT * 0.1)
            
            multi_sign = MathTex("\\times", color=MATRIX_A_COLOR).scale(0.65)
            multi_sign.next_to(matrix[entry][MATRIX_C_BOX_VGROUP], ORIGIN)
            
            transform_animations.append(Transform(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP], c_value))
            
            fade_in_animations.append(FadeIn(multi_sign, shift=DOWN))
            
            fade_out_animations.append(FadeOut(multi_sign, shift=UP))

        return transform_animations, fade_in_animations, fade_out_animations