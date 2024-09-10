from manim import ArcBetweenPoints, MoveAlongPath, VGroup, Rectangle, Scene, Text, FadeIn, FadeOut, MathTex, np, PI, RED_E, WHITE, RIGHT, ORIGIN, UL, UR, DOWN, LEFT, UP
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
    
#Scene 1

#Creates Matrix A with "boxes" with enteries
def createMatrixAScene1():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_A_NUMBERS[i], MATRIX_A_COLOR))
    
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates Matrix B with "boxes" with enteries
def createMatrixBScene1():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_B_NUMBERS[i], MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates a Matrix C with blank "boxes"
def createMatrixCScene1():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createBlankMatrixEntries())
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    return matrix

#Scene 2

#Create Matrix C with numbers from Matrix A & C
def createMatrixCScene2():
    matrix = VGroup()
    box_list = []
    
    for i in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createTwoMatrixEntries(MATRIX_A_NUMBERS[i], MATRIX_B_NUMBERS[i], MATRIX_A_COLOR, MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix
    
class Fox(Scene):
    def construct(self):
        #Scene 1 - Fade in matrices & signs - Move Matrix A & B enteries to Matrix C
        
        #Intialize Matrices
        matrixA_scene1 = createMatrixAScene1()
        matrixB_scene1 = createMatrixBScene1()
        matrixC_scene1 = createMatrixCScene1()
        
        #Intialize Signs
        multi_sign = MathTex("\\times")
        equal_sign = MathTex("=")
        
        matrices = VGroup(
            matrixA_scene1,
            multi_sign,
            matrixB_scene1,
            equal_sign,
            matrixC_scene1
        ).arrange(RIGHT, buff=MATRIX_BUFFER)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(1)
        
        #Align positions of enteries for Matrix A & B to Matrix C
        animations = []
        for i in range(MATRIX_ROW_COL_CT**2):
            numbers = matrixA_scene1[i][1]
            box_center = matrixC_scene1[i].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numbers.animate.move_to(target_position)) 
            
            numbers = matrixB_scene1[i][1]
            box_center = matrixC_scene1[i].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numbers.animate.move_to(target_position)) 
            
        
        self.play(*animations)
        
        #Scene 2 - Fade out Scene 1 Matrices - Fade in Scene 2 Matrix C - Move Matrix C to center
        LEFT_ALINGMENT = 2.15
        
        #Intialize Matrices for Scene 2
        matrixC_scene2 = createMatrixCScene2()
        self.add(matrixC_scene2)
            
        self.play(
            FadeOut(matrices),
            FadeIn(matrixC_scene2.shift(RIGHT * 4.27)),
        )
        matrices.remove(matrixA_scene1, matrixB_scene1, matrixC_scene1, equal_sign, multi_sign)
        
        self.wait(0.5)
        
        #Align position of Matrix C to move to Center
        animations = []
        for i in range((MATRIX_ROW_COL_CT**2)):
            
            #Matrix C
            boxes = matrixC_scene2[i][0]
            box_center = matrixB_scene1[i].get_center()
            target_position = box_center + ORIGIN
            animations.append(boxes.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
            
            #Enteries 1
            numbers = matrixC_scene2[i][1]
            box_center = matrixB_scene1[i].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))   
                
            #Enteries 2
            numbers = matrixC_scene2[i][2]
            box_center = matrixB_scene1[i].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
        
        self.play(*animations)
        
        self.wait(0.5)
        
        #Scene 3
        RIGHT_ALINGMENT = 0.3    
    
        #Copy Matrix C Values
        matrixC_copy = []
        for i in range(MATRIX_ROW_COL_CT**2):
            matrixC_copy.append(matrixC_scene2[i][1].copy())
            self.add(matrixC_copy[i])
    
        #Set Animations for Matrix Entreries (1) to move 
        animations = []
        
        while i < MATRIX_ROW_COL_CT:
            if i == 0:
                for n in range(MATRIX_ROW_COL_CT - 1):
                    arcPath = ArcBetweenPoints(matrixC_copy[n].get_center(), matrixC_copy[n + 1].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    animations.append(MoveAlongPath(matrixC_copy[n], arcPath))
                    
            elif i == MATRIX_ROW_COL_CT - 1:
                print("X")
                for n in range(MATRIX_ROW_COL_CT - 1, -1):
                    arcPath = ArcBetweenPoints(matrixC_copy[n].get_center(), matrixC_copy[n - 1].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    animations.append(MoveAlongPath(matrixC_copy[n], arcPath))
            else:
                arcPath = ArcBetweenPoints(matrixC_copy[i + MATRIX_ROW_COL_CT].get_center(), matrixC_copy[i + MATRIX_ROW_COL_CT - 1].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
            
            i += 1
                    
        '''
        arcPath = ArcBetweenPoints(matrixC_copy[0].get_center(), matrixC_copy[1].get_center(), angle=PI/2)
        animations = [
            MoveAlongPath(matrixC_copy[0], arcPath),
            matrixC_scene2[0][1].animate.move_to(matrixC_scene2[1][1]),
            matrixC_scene2[0][1].animate.move_to(matrixC_scene2[2][1]),
            matrixC_scene2[4][1].animate.move_to(matrixC_scene2[3][1]),
            matrixC_scene2[4][1].animate.move_to(matrixC_scene2[5][1]),
            matrixC_scene2[8][1].animate.move_to(matrixC_scene2[6][1]),
            matrixC_scene2[8][1].animate.move_to(matrixC_scene2[7][1])
        ]
        '''
        
        self.play(*animations, runtime = 5)
        self.wait(1)
        
        '''
        arcPath = ArcBetweenPoints(matrixC_scene2[3][1].get_center(), matrixC_scene2[5][1].get_center(), angle=PI/2)
        animations = [
            MoveAlongPath(matrixC_scene2[3][1], arcPath),
            matrixC_scene2[4][1].animate.move_to(matrixC_scene2[3][1]),
            matrixC_scene2[5][1].animate.move_to(matrixC_scene2[4][1]),
        ]
        
        self.play(*animations, runtime = 1)
        '''