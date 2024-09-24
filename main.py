from manim import ArcBetweenPoints, MoveAlongPath, VGroup,Scene, FadeIn, FadeOut, MathTex, np, PI, RIGHT, ORIGIN, LEFT
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.intial import *
from scenes.scene1 import *
from scenes.scene2 import *

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
        LEFT_ALINGMENT = 1.5
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
            
            #Enteries A
            numbers = matrixC_scene2[entry][1]
            box_center = matrixB_scene1[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))   
                
            #Enteries B
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
        fade_in_animations, fade_out_animations = updateABValuesToC(matrixC_scene2, matrixC_copy) or ([], [])
        self.play(*fade_in_animations)
        self.wait(1)
        self.play(*fade_out_animations)
        self.wait(1)
        
        