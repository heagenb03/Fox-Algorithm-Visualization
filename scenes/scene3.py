from manim import ArcBetweenPoints, MoveAlongPath, MathTex, FadeOut, FadeIn, PI, RIGHT, DR, UP, Text, Transform
import numpy as np
from constants import *
from intial import *

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.moved_aij_values = []
        self.temp_computed_c_values = []
        self.computed_c_values = self.intial.returnComputedCAsArray()
        self.entry_b_values = MATRIX_B_NUMBERS.copy()
    
    def moveBvalues(self, matrix):
        """Move Bij values up/down based on the row

        Args:
            matrix (VGroup): Matrix used in the scene

        Return:
            list: List of animations that move the Bij values up/down
        """
        move_animations = []
        temp_b_values = self.entry_b_values.copy()
        
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = col
                    final_point_entry = col + (MATRIX_ROW_COL_CT * (MATRIX_ROW_COL_CT - 1))
                    
                    arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center(), angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
                    
                    self.entry_b_values.insert(final_point_entry, temp_b_values[intial_entry])
                    self.entry_b_values.pop(final_point_entry + 1)
                    
            #Rest of the Rows
            else:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = (col + (row * MATRIX_ROW_COL_CT))
                    final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
                    
                    arcPath = ArcBetweenPoints(matrix[intial_entry][2].get_center(), matrix[final_point_entry][2].get_center(), angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][2], arcPath))
                    
                    self.entry_b_values.insert(final_point_entry, temp_b_values[intial_entry])
                    self.entry_b_values.pop(final_point_entry + 1)
    
        return move_animations
    
    def moveEnteriesToOwnBox(self, matrix, entry):
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
        
        arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
        move_animations.append(MoveAlongPath(temp_moved_aij_values[0], arcPath))

        fade_out_animations.append(FadeOut(temp_moved_aij_values[0]))
        
        return move_animations, fade_out_animations
        
    def moveEnteriesAcrossRight(self, matrix, entry):
        """Move All Aij values to the right

        Args:
            matrix (VGroup): Matrix used in the scene
            entry (int): index of the entry in the matrix

        Returns:
            list: List of animations that move the Aij values to the right, list of animations that fade out the temporary Aij values that moved
        """
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        count = 0
        for column in range(MATRIX_ROW_COL_CT - 1):
            final_point_entry = entry + column + 1
            temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count]))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

        return move_animations, fade_out_animations
    
    def moveEnteriesAcrossLeft(self, matrix, entry):
        """Move All Aij values to the left

        Args:
            matrix (VGroup): Matrix used in the scene
            entry (int): index of the entry in the matrix

        Returns:
            list: List of animations that move the Aij values to the left, list of animations that fade out the temporary Aij values that moved
        """
        move_animations = []
        fade_out_animations = []
        temp_moved_aij_values = []
        
        count = 0
        for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
            final_point_entry = entry - column
            temp_moved_aij_values.append(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].copy())
            
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count]))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))
        
        return move_animations, fade_out_animations
    
    def moveEnteriesAcrossRightAndLeft(self, matrix, entry, row):
        """Move All Aij values to the righ and left based on its position

        Args:
            matrix (VGroup): Matrix used in the scene
            entry (int): index of the entry in the matrix

        Returns:
            list: List of animations that move the Aij values to the right/left, list of animations that fade out the temporary Aij values that moved
        """
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
            
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count]))
            
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        #Columns in front of intial position
        for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
            final_point_entry = entry + front_column + 1
        
            arcPath = ArcBetweenPoints(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(temp_moved_aij_values[count], arcPath))
        
            fade_out_animations.append(FadeOut(temp_moved_aij_values[count]))
        
            self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))

            count += 1
            
        self.moved_aij_values.append(int(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_text()))
        
        return move_animations, fade_out_animations
    
    def updateComputedCValues(self, matrix):
        """Compute Cij values by multiplying Aij and Bij values and adding them to the computed C values; update the matrix with the new values

        Args:
            matrix (VGroup): Matrix used in the scene

        Returns:
            list: List of animations that update the matrix with the new Cij values, list of animations that fade in the multi sign, list of animations that fade out the multi sign
        """
        self.temp_computed_c_values = np.array(self.moved_aij_values) * np.array(self.entry_b_values)
        self.computed_c_values += self.temp_computed_c_values
        
        alingment = DOWN * 0.28 + RIGHT * 0.23
        
        transform_animations = []
        intial_move_animations = []
        final_move_animations = []
        intial_fade_in_animations = []
        final_fade_in_animations = []
        intial_fade_out_animations = []
        final_fade_out_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            c_value = Text(str(self.computed_c_values[entry]), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR, fill_opacity=MATRIX_TEXT_OPACITY)
            temp_c_value = Text(str(self.temp_computed_c_values[entry]), font_size=MATRIX_FONT_SIZE, color=C_VALUES_COLOR, fill_opacity=MATRIX_TEXT_OPACITY)
            moved_aij_value = Text(str(self.moved_aij_values[entry]), font_size=MATRIX_FONT_SIZE, color=MATRIX_A_COLOR, fill_opacity=MATRIX_TEXT_OPACITY)
            bij_value = Text(str(self.entry_b_values[entry]), font_size=MATRIX_FONT_SIZE, color=MATRIX_B_COLOR, fill_opacity=MATRIX_TEXT_OPACITY)
            
            moved_aij_value.align_to(matrix[entry][MATRIX_C_ENTRY_AIJ_MOVED_VGROUP], DL)
            bij_value.next_to(matrix[entry][MATRIX_C_BOX_VGROUP], UL).shift(DOWN * 0.6 + RIGHT * 1.1)
            
            multi_sign = MathTex("\\times", color=MATRIX_A_COLOR).scale(0.65)
            multi_sign.next_to(matrix[entry][MATRIX_C_BOX_VGROUP], ORIGIN)
            
            intial_fade_in_animations.append(FadeIn(multi_sign))
            
            intial_move_animations.append(moved_aij_value.animate.move_to(multi_sign.get_center()))
            intial_move_animations.append(bij_value.animate.move_to(multi_sign.get_center()))
            
            final_fade_in_animations.append(FadeIn(temp_c_value.next_to(matrix[entry][MATRIX_C_BOX_VGROUP], ORIGIN)))
            
            final_move_animations.append(temp_c_value.animate.move_to(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP].get_center()))
            
            transform_animations.append(Transform(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP], c_value.next_to(matrix[entry][MATRIX_C_BOX_VGROUP], ORIGIN).shift(alingment)))
            
            intial_fade_out_animations.append(FadeOut(multi_sign))
            intial_fade_out_animations.append(FadeOut(moved_aij_value))
            intial_fade_out_animations.append(FadeOut(bij_value))
            
            final_fade_out_animations.append(FadeOut(temp_c_value))

        return transform_animations, intial_move_animations, final_move_animations, intial_fade_in_animations, final_fade_in_animations, intial_fade_out_animations, final_fade_out_animations