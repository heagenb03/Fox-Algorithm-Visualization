from manim import Rectangle, VGroup, Text, MathTex, FadeIn, FadeOut, RED_E, WHITE, YELLOW, DOWN, RIGHT, UL, UR, DR, LEFT, UP
from constants import *

#Intialize Basic Callback Functions

#Creates the individual "box" within a matrix
def createMatrixBox():
    matrixBox = Rectangle(
            height=1,
            width=1,
            fill_color=RED_E,
            fill_opacity=0.7,
            stroke_color=WHITE
        )
    
    return matrixBox

#Intializes the "box" as empty
def createBlankMatrixEntries():
    result = VGroup() 
    result.add(createMatrixBox())
    
    return result

#Intailizes a "box" with one entry
def createMatrixEntry(num, txt_color):
    result = VGroup()
    box = createMatrixBox()
    
    entry = Text(str(num), font_size=MATRIX_FONT_SIZE, color=txt_color, fill_opacity=0.9)
    
    result.add(box, entry)
    
    return result

#Intailize a "box" with two enteries
def createTwoMatrixEntries(first_num, second_num, first_txt_color, second_txt_color):
    DOWN_ALINGMENT = 0.1
    SIDE_ALINGMENT = 0.1
    
    result = VGroup()
    box = createMatrixBox()
    
    first_entry = Text(str(first_num), font_size=MATRIX_FONT_SIZE, color=first_txt_color, fill_opacity=0.9)
    second_entry = Text(str(second_num), font_size=MATRIX_FONT_SIZE, color=second_txt_color, fill_opacity=0.9)
    first_entry.align_to(box, UL).shift(DOWN * DOWN_ALINGMENT + RIGHT * SIDE_ALINGMENT)
    second_entry.align_to(box, UR).shift(DOWN * DOWN_ALINGMENT + LEFT * SIDE_ALINGMENT)
    
    result.add(box, first_entry, second_entry)
    
    return result

#Creates a copy of the entries in the matrix to be used for animations
def createMatrixCopy(matrix):
    matrix_copy = []
    for column in range(MATRIX_ROW_COL_CT - 1):
        for box in range(MATRIX_ROW_COL_CT**2):
            matrix_copy.append(matrix[box][1].copy())
            
    return matrix_copy

#Updates the values of the matrix C by the product of the values of matrix A(i) and B values to create C values
def updateABValuesToC(matrix, matrix_copy):
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
        
        entry_c = Text(str(value_c), font_size=MATRIX_FONT_SIZE, color=YELLOW)
        entry_c.align_to(box[0], DR).shift(UP * UP_ALINGMENT + LEFT * LEFT_ALINGMENT)
        
        box.add(multi_sign, entry_c)
        
        fade_in_animations.append(FadeIn(multi_sign))
        fade_in_animations.append(FadeIn(entry_c))
        
        fade_out_animations.append(FadeOut(multi_sign))
        fade_out_animations.append(FadeOut(box[2])) #Entry B
        fade_out_animations.append(FadeOut(matrix_copy[col * (row + 1)])) #Entry A
        
        if col == MATRIX_ROW_COL_CT - 1:
            col = 0
            row += 1
        else:
            col += 1
            
    return fade_in_animations, fade_out_animations
            