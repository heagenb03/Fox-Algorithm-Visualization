from manim import VGroup, Scene, FadeIn, FadeOut, MathTex, RendererType, RIGHT, ORIGIN
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.intial import Intial
from scenes.scene1 import Scene1
from scenes.scene2 import Scene2
from scenes.scene3 import Scene3
from scenes.scene4 import Scene4

class Fox(Scene):
    def construct(self):
        #Scene 1 - Fade in matrices & signs - Move Matrix A & B enteries to Matrix C        
        
        intial = Intial()
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        scene4 = Scene4()
        
        self.multi_sign = MathTex("\\times")
        self.equal_sign = MathTex("=")
        
        #Intialize Matrices
        matrixA_scene1 = scene1.createMatrixA()
        matrixB_scene1 = scene1.createMatrixB()
        matrixC_scene1 = scene1.createMatrixC()
        
        matrices = VGroup(
            matrixA_scene1,
            self.multi_sign,
            matrixB_scene1,
            self.equal_sign,
            matrixC_scene1
        ).arrange(RIGHT, buff=MATRIX_BUFFER)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(1)
            
        move_animations = scene1.moveEnteriesToMatrixC(matrixA_scene1, matrixB_scene1, matrixC_scene1)
        self.play(*move_animations)
        
        #Scene 2 - Fade out Scene 1 Matrices - Fade in Scene 2 Matrix C - Move Matrix C to center
        
        matrixC_scene2 = scene2.createMatrixC()
        self.add(matrixC_scene2)
            
        self.play(
            FadeOut(matrices),
            FadeIn(matrixC_scene2.shift(RIGHT * scene2.RIGHT_ALINGMENT)),
        )
        self.wait(0.5)
        
        move_animations = scene2.moveMatrixCtoCenter(matrixB_scene1, matrixC_scene2)
        matrices.remove(matrixA_scene1, matrixB_scene1, matrixC_scene1, self.equal_sign, self.multi_sign)
        
        self.play(*move_animations)
        self.wait(0.5)
        
        #Scene 3 - Start Step 1 of the Fox Algorithm process 
            # - Move Matrix C first row entries to the right - Move Matrix C middle rows to respective left and right - Move Matrix C last row entries to the left
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            #Set Animations for Matrix Entries Aij to move - Matrix C copies for animations - Matrix C of distrubited Aij values
            
            '''
            matrixA_copy, matrixB_copy = intial.createMatrixCopy(matrixC_scene2)
            matrixC_of_Aij_values = []
            total_animations = []
            
            scene3.moveEnteries(matrixC_scene2, shift_count)
            
            for row in range(MATRIX_ROW_COL_CT):
                #Entries move accross the row to the right
                if row == 0:
                    intial_entry =  row + (row * (MATRIX_ROW_COL_CT**2)) + shift_count
                    
                    move_animations, aij_values = scene3.moveEnteriesAcrossRight(row, matrixA_copy, intial_entry)
                    
                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
                    
                #Entries move across the row to the left
                elif row == MATRIX_ROW_COL_CT - 1:
                    move_animations, aij_values = scene3.moveEnteriesAcrossLeft(row, matrixA_copy)

                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
        
                #Entries move across the row to the right and left
                else:
                    move_animations, aij_values = scene3.moveEnteriesAcrossLeftAndRight(row, matrixA_copy)
                
                    total_animations += move_animations
                    matrixC_of_Aij_values += aij_values
            
            self.play(*total_animations, runtime=5)
            self.wait(1)
            '''
            
            #Scene 4 - Start Step 2 of the Fox Algorithm process - Move Matrix Bij values one row up if applicable - Multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            
            #Move Matrix Bij values one row up if applicable
            move_animations, matrixC_scene2 = scene4.moveBvalues(shift_count, matrixC_scene2)
            
            if shift_count != 0:
                self.play(*move_animations, runtime=5)
                
            self.wait(1)
            
            #Intialize animations to multiply Matrix Aij values with Matrix Bij values to create new Matrix C values
            fade_in_animations, fade_out_animations = scene4.updateABValuesToC(matrixC_scene2)
            
            self.play(*fade_in_animations, runtime=5)
            self.wait(1)
            self.play(*fade_out_animations, runtime=5)
            self.wait(1)
        
            shift_count += 1