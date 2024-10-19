from manim import Rectangle, VGroup, Text, UP, DOWN, RIGHT, UL, UR, DR, DL, LEFT
from constants import *

#Intialize functions utilized in the scenes
class Intial:
    def __init__(self):
        self.VERT_ALINGMENT = 0.1
        self.HORIZONTAL_ALINGMENT = 0.1
    
    def createMatrixBox(self):
        """Create a the individual "box" within a matrix

        Returns:
            Rectangle: matrix box
        """
        box = Rectangle(
                height=1,
                width=1,
                fill_color=MATRIX_BG_COLOR,
                fill_opacity=0.7,
                stroke_color=MATRIX_BORDER_COLOR
            )
        
        return box

    def createBlankMatrixEntries(self):
        """Create a matrix box with no entry

        Returns:
            VGroup: VGroup with matrix box
        """
        result = VGroup()
        box = self.createMatrixBox()
        
        result.add(box)
        return result

    def createMatrixEntry(self, num, txt_color):
        """Create a matrix box with one entry

        Args:
            num (int/float): number to be displayed in the box
            txt_color (str): text color

        Returns:
            VGroup: VGroup with matrix box and entry with number
        """
        result = VGroup()
        matrix_box = self.createMatrixBox()
        
        entry = Text(str(num), font_size=MATRIX_FONT_SIZE, color=txt_color, fill_opacity=MATRIX_TEXT_OPACITY)
        result.add(matrix_box, entry)
        
        return result

    def createMatrixFourEntries(self, first_num, second_num, third_num, fourth_num, first_txt_color, second_txt_color, third_txt_color):
        """Create a matrix box with four entries 

        Args:
            first_num (int/float): Aij values from Matrix A
            second_num (int/float): Bij values from Matrix B
            third_num (int/float): Temporary values from the moved Aij values
            fourth_num (int/float): Computed Cij values from Aij * Bij
            first_txt_color, second_txt_color, third_text_color (str): according text colors

        Returns:
            VGroup: VGroup with matrix box and four entries
        """
        result = VGroup()
        matrix_box = self.createMatrixBox()
        
        first_entry = Text(str(first_num), font_size=MATRIX_FONT_SIZE, color=first_txt_color, fill_opacity=MATRIX_TEXT_OPACITY)
        second_entry = Text(str(second_num), font_size=MATRIX_FONT_SIZE, color=second_txt_color, fill_opacity=MATRIX_TEXT_OPACITY)
        third_entry = Text('', font_size=MATRIX_FONT_SIZE, color=first_txt_color, fill_opacity=MATRIX_TEXT_OPACITY) #Entry the Moved Aij values go to
        fourth_entry = Text(str(fourth_num), font_size=MATRIX_FONT_SIZE, color=third_txt_color, fill_opacity=MATRIX_TEXT_OPACITY) #Computed C Values go to
        
        first_entry.align_to(matrix_box, UL).shift(DOWN * self.VERT_ALINGMENT + RIGHT * self.HORIZONTAL_ALINGMENT)
        second_entry.align_to(matrix_box, UR).shift(DOWN * self.VERT_ALINGMENT + LEFT * self.HORIZONTAL_ALINGMENT)
        third_entry.align_to(matrix_box).shift(UP * self.VERT_ALINGMENT + RIGHT * self.HORIZONTAL_ALINGMENT)
        fourth_entry.align_to(matrix_box, DR).shift(UP * self.VERT_ALINGMENT + LEFT * self.HORIZONTAL_ALINGMENT)
        
        result.add(matrix_box, first_entry, second_entry, third_entry, fourth_entry)
        return result