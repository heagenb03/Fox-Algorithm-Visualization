from manim import VGroup, Rectangle, Scene, Text, RED_E, WHITE, YELLOW, RIGHT, ORIGIN, FadeIn
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

#Intailizes a "box" with one entry
def createMatrixEntry(num, txt_color):
    result = VGroup()
    entry = Text(str(num), font_size=MATRIX_FONT_SIZE, color=txt_color)
    
    result.add(createMatrixBox(), entry)
    
    return result

#Intailize a "box" with two enteries
def createTwoMatrixEntries(first_num, second_num, first_txt_color, second_txt_color):
    result = VGroup()
    box = createMatrixBox()
    
    first_entry = Text(str(first_num), font_size=MATRIX_FONT_SIZE, color=first_txt_color)
    second_entry = Text(str(second_num), font_size=MATRIX_FONT_SIZE, color=second_txt_color)
    first_entry.align_to(box, UL).shift(DOWN * 0.1 + RIGHT * 0.1)
    second_entry.align_to(box, UR).shift(DOWN * 0.1 + LEFT * 0.1)
    
    result.add(box, first_entry, second_entry)
    
    return result
    
#Scene 1

#Creates Matrix A with "boxes" with enteries
def createMatrixAScene1():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_COL_CT*MATRIX_ROW_CT):
        box_list.append(createMatrixEntry(MATRIX_A_NUMBERS[i], MATRIX_A_COLOR))
    
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates Matrix B with "boxes" with enteries
def createMatrixBScene1():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_COL_CT*MATRIX_ROW_CT):
        box_list.append(createMatrixEntry(MATRIX_B_NUMBERS[i], MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates a Matrix C with blank "boxes"
def createMatrixCScene1():
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
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=MATRIX_BUFFER)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=0.25)
    return matrix


class Fox(Scene):
    def construct(self):
        matrixA = createMatrix(WHITE)
        matrixB = createMatrix(YELLOW)
        matrixC = createBlankMatrix()
        
        matrices = VGroup(
            matrixA_scene1,
            multi_sign,
            matrixB_scene1,
            equal_sign,
            matrixC_scene1
        ).arrange(RIGHT, buff=0.25)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(1)
        
        animations = []
        for i in range(MATRIX_ROW_CT*MATRIX_COL_CT):
            numberes = matrixA_scene1[i][1]
            box_center = matrixC_scene1[i].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numberes.animate.move_to(target_position)) 
            
            numberes = matrixB_scene1[i][1]
            box_center = matrixC_scene1[i].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numberes.animate.move_to(target_position)) 
            
        self.play(*animations)
        self.wait(1)
        
        #Scene 2
        matrixC_scene2 = createMatrixCScene2()
        
        self.play(FadeIn(matrices))
        self.wait(2)
        self.play(
            FadeIn(matrices)
        )
        
        self.wait(1)