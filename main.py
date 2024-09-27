from manim import ArcBetweenPoints, MoveAlongPath, VGroup,Scene, FadeIn, FadeOut, MathTex, np, PI, RIGHT, ORIGIN, LEFT
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.intial import *
from scenes.scene1 import *
from scenes.scene2 import *
from scenes.scene3 import *
from scenes.scene4 import * 

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
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrixA_scene1[entry][1]
            box_center = matrixC_scene1[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = box_center + offset
            move_animations.append(numbers.animate.move_to(target_position)) 
            
            numbers = matrixB_scene1[entry][1]
            box_center = matrixC_scene1[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = box_center + offset
            move_animations.append(numbers.animate.move_to(target_position)) 
            
        
        self.play(*move_animations)
        
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
        move_animations = []
        for entry in range((MATRIX_ROW_COL_CT**2)):
            
            #Matrix C
            boxes = matrixC_scene2[entry][0]
            box_center = matrixB_scene1[entry].get_center()
            target_position = box_center + ORIGIN
            move_animations.append(boxes.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
            
            #Enteries A
            numbers = matrixC_scene2[entry][1]
            box_center = matrixB_scene1[entry].get_center()
            offset = np.array([-0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))   
                
            #Enteries B
            numbers = matrixC_scene2[entry][2]
            box_center = matrixB_scene1[entry].get_center()
            offset = np.array([0.32, 0.28, 0])
            target_position = offset + box_center + ORIGIN
            move_animations.append(numbers.animate.move_to(target_position + LEFT * LEFT_ALINGMENT))
        
        self.play(*move_animations)
        
        self.wait(0.5)
        
        #Scene 3 - Start Step 1 of the Fox Algorithm process 
            # - Move Matrix C first row entries to the right - Move Matrix C middle rows to respective left and right - Move Matrix C last row entries to the left
        
        #Intialize alingment for Scene 3
        RIGHT_ALINGMENT = 0.3
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            #Set Animations for Matrix Entries Aij to move - Matrix C copies for animations - Matrix C of distrubited Aij values
            matrixA_copy, matrixB_copy = createMatrixCopy(matrixC_scene2)
            matrixC_of_Aij_values = []
            total_animations = []
            
            for row in range(MATRIX_ROW_COL_CT):
                #Entries move accross the row to the right
                if row == 0:
                    move_animations, aij_values = moveEnteriesAcrossRight(row, matrixA_copy, RIGHT_ALINGMENT)
                    
                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
                    
                #Entries move across the row to the left
                elif row == MATRIX_ROW_COL_CT - 1:
                    move_animations, aij_values = moveEnteriesAcrossLeft(row, matrixA_copy, RIGHT_ALINGMENT)

                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
        
                #Entries move across the row to the right and left
                else:
                    move_animations, aij_values = moveEnteriesAcrossLeftAndRight(row, matrixA_copy, RIGHT_ALINGMENT)
                
                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
            
            self.play(*total_animations, runtime=5)
            self.wait(1)
            
            #Scene 4 - Start Step 2 of the Fox Algorithm process - Move Matrix Bij values one row up if applicable - Multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            
            #Move Matrix Bij values one row up if applicable
            move_animations, fade_out_animations = moveBvalues(shift_count, matrixB_copy, matrixC_scene2)
            
            if shift_count != 0:
                self.play(*move_animations, *fade_out_animations, runtime=5)
                
            self.wait(1)
            
            #Intialize animations to multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            fade_in_animations, fade_out_animations = updateABValuesToC(matrixC_scene2, matrixC_of_Aij_values)
            
            self.play(*fade_in_animations, runtime=5)
            self.wait(1)
            self.play(*fade_out_animations, runtime=5)
            self.wait(1)
        
            shift_count += 1