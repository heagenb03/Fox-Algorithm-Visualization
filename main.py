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
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
                
            #Intialize alingment for Scene 3 - Matrix C copy for animations - Matrix C of distrubited Aij values
            RIGHT_ALINGMENT = 0.3    
            matrixA_copy, matrixB_copy = createMatrixCopy(matrixC_scene2)
            matrixC_of_Aij_values = []
            
            #Set Animations for Matrix Entreries (1) to move 
            animations = []
            for row in range(MATRIX_ROW_COL_CT):
                #First Row
                if row == 0:
                    #Gets each intial entry respective to the matrix copy and moves it across the row to the right
                    for column in range(MATRIX_ROW_COL_CT - 1):
                        intial_entry = row + (column * (MATRIX_ROW_COL_CT**2))
                        final_point_entry = row + (column + 1)
                        
                        arcPath = ArcBetweenPoints(matrixA_copy[intial_entry].get_center(), matrixA_copy[final_point_entry].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                        animations.append(MoveAlongPath(matrixA_copy[intial_entry], arcPath))
                        matrixC_of_Aij_values.append(matrixA_copy[intial_entry])
                
                #Last Row
                elif row == MATRIX_ROW_COL_CT - 1:
                    #Gets each intial entry respective to the matrix copy and moves it across the row to the left
                    for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
                        intial_entry = row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))
                        final_point_entry = (row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))) - column
                        
                        arcPath = ArcBetweenPoints(matrixA_copy[intial_entry].get_center(), matrixA_copy[final_point_entry].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                        animations.append(MoveAlongPath(matrixA_copy[intial_entry], arcPath))
                        matrixC_of_Aij_values.append(matrixA_copy[intial_entry])
                
                #Middle Rows
                else:
                    #Gets each intial entry respective to the matrix copy and moves it across the row to the right and left based on its intial position
                    #Columns behind intial position
                    for back_column in range(row):
                        intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))
                        
                        if back_column == 0:
                            final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column)) - 1
                            
                            arcPath = ArcBetweenPoints(matrixA_copy[intial_entry].get_center(), matrixA_copy[final_point_entry].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                        else:
                            final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column))
                            
                            arcPath = ArcBetweenPoints(matrixA_copy[intial_entry].get_center(), matrixA_copy[final_point_entry].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                        
                        animations.append(MoveAlongPath(matrixA_copy[intial_entry], arcPath))
                        matrixC_of_Aij_values.append(matrixA_copy[intial_entry])
                    
                    #Columns in front of intial position
                    for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
                        intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + ((front_column + back_column + 1) * (MATRIX_ROW_COL_CT**2))
                        final_point_entry = row + (row * (MATRIX_ROW_COL_CT + front_column)) + 1
                        
                        arcPath = ArcBetweenPoints(matrixA_copy[intial_entry].get_center(), matrixA_copy[final_point_entry].get_center() + RIGHT * RIGHT_ALINGMENT, angle=PI/2)
                        animations.append(MoveAlongPath(matrixA_copy[intial_entry], arcPath))
                        matrixC_of_Aij_values.append(matrixA_copy[intial_entry])
            
            self.play(*animations, runtime=5)
            self.wait(1)
            
            #Scene 4 - Start Step 2 of the Fox Algorithm process - Move Matrix Bij values one row up if applicable - Multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            
            #Move Matrix Bij values one row up if applicable
            animations = []
            if shift_count != 0:
                for row in range(MATRIX_ROW_COL_CT):
                    #First Row
                    if row == 0:
                        for col in range(1, MATRIX_ROW_COL_CT):
                            arcPath = ArcBetweenPoints(matrixB_copy[col + (row * MATRIX_ROW_COL_CT)].get_center(), matrixB_copy[row + ((col + 1) * MATRIX_ROW_COL_CT) + (MATRIX_ROW_COL_CT * (MATRIX_ROW_COL_CT - 1))].get_center() + ORIGIN, angle=PI/2)
                            animations.append(MoveAlongPath(matrixB_copy[col + (row * MATRIX_ROW_COL_CT)], arcPath))
            
                self.play(*animations, runtime=5)
            
            self.wait(1)
            
            #Intialize animations to multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            fade_in_animations, fade_out_animations = updateABValuesToC(matrixC_scene2, matrixC_of_Aij_values) or ([], [])
            
            self.play(*fade_in_animations, runtime=5)
            self.wait(1)
            self.play(*fade_out_animations, runtime=5)
            self.wait(1)
        
            
        
            shift_count += 1