from manim import VGroup, Rectangle, Scene, Text, RED_E, WHITE, RIGHT, ORIGIN, FadeIn, FadeOut, MathTex, np
from constants import *


#Intialize Basic Callback Functions

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
    for i in range(MATRIX_COL_CT*MATRIX_ROW_CT):
        box_list.append(createBlankMatrixEntries())
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    return matrix

#Scene 1

#Creates Matrix A with "boxes" with enteries
def createMatrixAScene1():
    matrix = VGroup()
    box_list = []
    for i in range(MATRIX_COL_CT*MATRIX_ROW_CT):
        box_list.append(createMatrixEntries(MATRIX_A_NUMBERS[i], MATRIX_A_COLOR))
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    return matrix

#Creates Matrix B with "boxes" with enteries
def createMatrixBScene1():
    matrix = VGroup()
    box_list = []
    for i in range(MATRIX_COL_CT*MATRIX_ROW_CT):
        box_list.append(createMatrixEntries(MATRIX_B_NUMBERS[i], MATRIX_B_COLOR))
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    return matrix

#Scene 2

#Create Matrix C with numbers from Matrix A & C
def createMatrixCScene2():
    matrix = VGroup()
    box_list = []
    
    

class Fox(Scene):
    def construct(self):
        #Scene 1 - Fade in matrices + signs & fade out matrixA, B, & signs
        
        #Intialize Matrices
        matrixA_scene1 = createMatrixAScene1()
        matrixB_scene1 = createMatrixBScene1()
        matrixC_scene1 = createBlankMatrix()
        
        #Intialize Signs
        multi_sign = MathTex("\\times")
        equal_sign = MathTex("=")
        
        matrices = VGroup(
            matrixA_scene1,
            multi_sign,
            matrixB_scene1,
            equal_sign,
            matrixC_scene1
        ).arrange(RIGHT, buff=0.25)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(2)
        self.play(
            FadeOut(multi_sign),
            FadeOut(equal_sign)
        )
        self.wait()
        
        animations = []
        for i in range(9):
            numberes = matrixA_scene1[i][1]
            box_center = matrixC_scene1[i].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numberes.animate.move_to(target_position)) 
            
            numberes = matrixB_scene1[i][1]
            box_center = matrixB_scene1[i].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numberes.animate.move_to(target_position)) 
            
        self.play(*animations)
        self.play(FadeOut(matrixA_scene1, matrixB_scene1))
        self.wait(2)
        
        #Scene 2
        