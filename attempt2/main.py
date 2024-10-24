from manim import VGroup, Scene, FadeIn, FadeOut, MathTex, RendererType, Text, RIGHT, LEFT, ORIGIN
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.intial import Intial
from scenes.scene1 import Scene1
from scenes.scene2 import Scene2
from scenes.scene3 import Scene3

class Fox(Scene):
    def construct(self):
        """
        Scene 1 
            #1. Create Matrix A, B, C
            #2. Move Aij & Bij values to corresponding Cij
        """
        
        #1
        intial = Intial()
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        
        multi_sign = MathTex("\\times")
        equal_sign = MathTex("=")
        
        matrixA_scene1 = scene1.createMatrixA()
        matrixB_scene1 = scene1.createMatrixB()
        matrixC_scene1 = scene1.createMatrixC()
        
        matrices = VGroup(
            matrixC_scene1,
            equal_sign,
            matrixB_scene1,
            multi_sign,
            matrixA_scene1
        ).arrange(LEFT, buff=MATRIX_BUFFER)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(1)
        
        #2
        move_animations = scene1.moveEnteriesToMatrixC(matrixA_scene1, matrixB_scene1, matrixC_scene1)
        self.play(*move_animations)
        self.wait(0.5)
        
        """
        Scene 2 
            1. Remove Matrix A, B
            2. Move Matrix C to center
        """
        
        #1
        matrixC_scene2 = scene2.createMatrixC()
        
        self.play(FadeOut(matrices),
                  FadeIn(matrixC_scene2.shift(RIGHT * scene2.RIGHT_ALINGMENT))
        )
        self.wait(0.5)
        
        #2
        move_animations = scene2.moveMatrixCtoCenter(matrixB_scene1, matrixC_scene2)
        self.play(*move_animations)
        self.wait(0.5)
        
        """
        Scene 3
            1. 
        """        
        matrixC_entryA_array = intial.retunMatrixAs2dArray(matrixC_scene2, MATRIX_C_ENTRY_A_VGROUP)
        matrixC_entryB_array = intial.retunMatrixAs2dArray(matrixC_scene2, MATRIX_C_ENTRY_B_VGROUP)
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            total_move_animations = []
            total_fade_out_animations = []
            scene3.moved_aij_values = []
            scene3.temp_computed_c_values = []
            
            for row in range(MATRIX_ROW_COL_CT):
                col = shift_count + row
                
                if col >= MATRIX_ROW_COL_CT:
                    col = abs(MATRIX_ROW_COL_CT - col)
                    
                move_entry_pos = (row * MATRIX_ROW_COL_CT) + col
                if col == 0:
                    move_animations, fade_out_animations = scene3.moveEnteriesAcrossRight(matrixC_scene2, move_entry_pos)
                    total_move_animations.extend(move_animations)
                    total_fade_out_animations.extend(fade_out_animations)
                    
                elif col == MATRIX_ROW_COL_CT - 1:
                    move_animations, fade_out_animations = scene3.moveEnteriesAcrossLeft(matrixC_scene2, move_entry_pos)
                    total_move_animations.extend(move_animations)
                    total_fade_out_animations.extend(fade_out_animations)
                    
                else:
                    move_animations, fade_out_animations = scene3.moveEnteriesAcrossRightAndLeft(matrixC_scene2, move_entry_pos, col)
                    total_move_animations.extend(move_animations)
                    total_fade_out_animations.extend(fade_out_animations)

            self.play(*total_move_animations)
            self.wait(1)
            
            transform_animations, move_animations = scene3.updateComputedCValues(matrixC_scene2)
            
            self.play(*transform_animations)
            self.wait(1)
            self.play(*move_animations, 
                      *total_fade_out_animations, runtime=5)
            self.wait(1)
            
            shift_count += 1
            
        