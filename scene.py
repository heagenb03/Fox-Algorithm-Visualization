from manim import ArcBetweenPoints, MoveAlongPath, VGroup, Rectangle, Scene, Text, FadeIn, FadeOut, MathTex, np, tempconfig, PI, RED_E, WHITE, RIGHT, ORIGIN, UL, UR, DOWN, LEFT, UP
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

#Scene 1

#Creates Matrix A with "boxes" with enteries
def createMatrixAScene1():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_A_NUMBERS[entry], MATRIX_A_COLOR))
    
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates Matrix B with "boxes" with enteries
def createMatrixBScene1():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createMatrixEntry(MATRIX_B_NUMBERS[entry], MATRIX_B_COLOR))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    
    return matrix

#Creates a Matrix C with blank "boxes"
def createMatrixCScene1():
    matrix = VGroup()
    box_list = []
    
    for box in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createBlankMatrixEntries())
    matrix.add(*box_list)
    
    matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
    return matrix

#Scene 2

#Create Matrix C with numbers from Matrix A & C
def createMatrixCScene2():
    matrix = VGroup()
    box_list = []
    
    for entry in range(MATRIX_ROW_COL_CT**2):
        box_list.append(createTwoMatrixEntries(MATRIX_A_NUMBERS[entry], MATRIX_B_NUMBERS[entry], MATRIX_A_COLOR, MATRIX_B_COLOR))
        
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
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrixA_scene1[entry][1]
            box_center = matrixC_scene1[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numbers.animate.move_to(target_position)) 
            
            numbers = matrixB_scene1[entry][1]
            box_center = matrixC_scene1[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            animations.append(numbers.animate.move_to(target_position)) 
            
        
        self.play(*animations)
        
        #Scene 2 - Fade out Scene 1 Matrices - Fade in Scene 2 Matrix C - Move Matrix C to center
        
         #Intialize alingment for Scene 2 and matrices for Scene 2
        LEFT_ALINGMENT = 2.15
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
        for entry in range((MATRIX_ROW_COL_CT**2)):
            
            #Matrix C
            boxes = matrixC_scene2[entry][0]
            box_center = matrixB_scene1[entry].get_center()
            target_position = box_center + ORIGIN
            animations.append(boxes.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
            
            #Enteries 1
            numbers = matrixC_scene2[entry][1]
            box_center = matrixB_scene1[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))   
                
            #Enteries 2
            numbers = matrixC_scene2[entry][2]
            box_center = matrixB_scene1[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
        
        self.play(*animations)
        
        self.wait(0.5)
        
        #Scene 3 - Start Step 1 of the Fox Algorithm process 
            # - Move Matrix C first row entries to the right - Move Matrix C middle rows to respective left and right - Move Matrix C last row entries to the left
        
        #Intialize alingment for Scene 3 & Matrix C copy for animations
        RIGHT_ALINGMENT = 0.3    
        matrixC_copy = createMatrixCopy(matrixC_scene2)
        
        #Set Animations for Matrix Entreries (1) to move 
        animations = []
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                #Gets each intial entry respective to the matrix copy and moves it across the row to the right
                for column in range(MATRIX_ROW_COL_CT - 1):
                    arcPath = ArcBetweenPoints(matrixC_copy[row + (column * (MATRIX_ROW_COL_CT**2))].get_center(), matrixC_copy[row + (column + 1)].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    animations.append(MoveAlongPath(matrixC_copy[row + (column * (MATRIX_ROW_COL_CT**2))], arcPath))
              
            #Last Row
            elif row == MATRIX_ROW_COL_CT - 1:
                #Gets each intial entry respective to the matrix copy and moves it across the row to the left
                for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
                    arcPath = ArcBetweenPoints(matrixC_copy[row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))].get_center(), matrixC_copy[(row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))) - column].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    animations.append(MoveAlongPath(matrixC_copy[row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))], arcPath))
            
            #Middle Rows
            else:
                #Gets each intial entry respective to the matrix copy and moves it across the row to the right and left based on its intial position
                #Columns behind intial position
                for back_column in range(row):
                    if back_column == 0:
                        arcPath = ArcBetweenPoints(matrixC_copy[(row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))].get_center(), matrixC_copy[row + (row * (MATRIX_ROW_COL_CT - back_column)) - 1].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    else:
                        arcPath = ArcBetweenPoints(matrixC_copy[(row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))].get_center(), matrixC_copy[row + (row * (MATRIX_ROW_COL_CT - back_column))].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    
                    animations.append(MoveAlongPath(matrixC_copy[(row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))], arcPath))
                
                #Columns in front of intial position
                for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
                    arcPath = ArcBetweenPoints(matrixC_copy[(row + (row * MATRIX_ROW_COL_CT)) + ((front_column + back_column + 1) * (MATRIX_ROW_COL_CT**2))].get_center(), matrixC_copy[row + (row * (MATRIX_ROW_COL_CT + front_column)) + 1].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                    animations.append(MoveAlongPath(matrixC_copy[(row + (row * MATRIX_ROW_COL_CT)) + ((front_column + back_column + 1) * (MATRIX_ROW_COL_CT**2))], arcPath))
        
        self.play(*animations, runtime = 5)
        self.wait(1)
        
        #Scene 4 - Start Step 2 of the Fox Algorithm process
        
        #Intialize Signs
        multi_sign = MathTex("\\times")
        
        
with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = Fox()
    scene.render()