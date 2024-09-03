from manim import VGroup, Rectangle, Scene, Text, RED_E, WHITE, YELLOW, RIGHT, ORIGIN, FadeIn
from constants import *

#Creates the individual "box" within a matrix
def createMatrixBox():
    matrixBox = Rectangle(
            height=1,
            width=1,
            fill_color=RED_E,
            fill_opacity=0.8,
            stroke_color=WHITE
        )
    
    return matrixBox

#Intializes the "box" as empty
def createBlankMatrixEntries():
    result = VGroup() 
    result.add(createMatrixBox())
    return result

#Intailizes a "box" with entries
def createMatrixEntries(number, textColor):
    result = VGroup()
    entry = Text(str(number), font_size=24, color=textColor)
    result.add(createMatrixBox(), entry)
    return result

#Creates a Matrix with blank "boxes"
def createBlankMatrix():
    matrix = VGroup()
    box_list = []
    for i in range(MATRIX_SIZE):
        box_list.append(createBlankMatrixEntries())
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=0.25)
    return matrix

#Creates a Matrix with "boxes" with enteries
def createMatrix(textColor):
    matrix = VGroup()
    box_list = []
    for i in range(MATRIX_SIZE):
        box_list.append(createMatrixEntries(i, textColor))
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=0.25)
    return matrix


class Fox(Scene):
    def construct(self):
        matrixA = createMatrix(WHITE)
        matrixB = createMatrix(YELLOW)
        matrixC = createBlankMatrix()
        
        matrices = VGroup(
            matrixA,
            matrixB,
            matrixC
        ).arrange(RIGHT, buff=0.25)
        
        matrices.move_to(ORIGIN)
        
        self.play(
            FadeIn(matrices)
        )
        