from manim import VGroup, Scene, FadeIn, FadeOut, MathTex, RendererType, Text, RIGHT, LEFT, ORIGIN
import numpy as np
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
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        scene4 = Scene4()
        
        """
        Scene 1 
            #1. Create Matrix A, B, C
            #2. Move Aij & Bij values to corresponding Cij values / Fadeout Matrix A & B
        """
        
        #1        
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
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        
        matrices.move_to(ORIGIN)
        
        self.play(FadeIn(matrices))
        self.wait(5)
        
        #2
        move_animations = scene1.moveEnteriesToMatrixC(matrixA_scene1, matrixB_scene1, matrixC_scene1)
        self.play(*move_animations)
        self.wait(0.5)
        
        partial_matrixC_scene = scene1.createPartialMatrixC()
        
        self.play(FadeOut(matrices),
                FadeIn(partial_matrixC_scene.shift(RIGHT * scene1.RIGHT_ALINGMENT))
        )
        self.wait(0.5)
        
        """
        Scene 2 
            1. Move Matrix C to center
            2. Realign Matrix C for future animation purposes
        """
        
        #1
        matrixC_scene2 = scene2.createMatrixC()


        move_animations = scene2.moveMatrixCtoCenter(matrixB_scene1, partial_matrixC_scene)
        self.play(*move_animations)
        self.play(FadeOut(partial_matrixC_scene),
                FadeIn(matrixC_scene2.shift(RIGHT * scene2.RIGHT_ALINGMENT))
        )
        
        #2
        adjust_animations = scene2.realignMatrixC(matrixC_scene2)
        self.play(*adjust_animations)
        
        self.wait(1)
        
        """
        Scene 3
            1. Move Bij values up/down one row 
            2. Move Aij values to the right/left
            3. Update Cij values after movement of Bij and Aij values
        """         
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            total_move_animations = []
            total_fade_out_animations = []
            
            #1
            if shift_count != 0:
                scene3.moved_aij_values = []
                scene3.temp_computed_c_values = []
                
                move_animations = scene3.moveBvalues(matrixC_scene2)
                
                self.play(*move_animations)
                self.wait(1)
            
            #2
            for row in range(MATRIX_ROW_COL_CT):
                col = shift_count + row
                
                if col >= MATRIX_ROW_COL_CT:
                    col = abs(MATRIX_ROW_COL_CT - col)
                    
                move_entry_pos = (row * MATRIX_ROW_COL_CT) + col
                
                move_animations, fade_out_animations = scene3.moveEnteriesToOwnBox(matrixC_scene2, move_entry_pos)
                total_move_animations.extend(move_animations)
                total_fade_out_animations.extend(fade_out_animations)
                
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
            
            #3
            transform_animations, intial_move_animations, final_move_animations, intial_fade_in_animations, final_fade_in_animations, intial_fade_out_animations, final_fade_out_animations = scene3.updateComputedCValues(matrixC_scene2)
            total_fade_out_animations.extend(final_fade_out_animations)
            
            self.play(*intial_fade_in_animations)
            self.wait(1)
            self.play(*intial_move_animations)
            self.wait(0.15)
            self.play(*final_fade_in_animations,
                      *intial_fade_out_animations)
            self.wait(1)
            self.play(*final_move_animations)
            self.wait(0.25)
            self.play(*transform_animations,
                      *total_fade_out_animations)
            self.wait(2)
            
            shift_count += 1
        
        """
        Scene 4
            1. Display finished Matrix C
            2. Return to intial state of Matrix A, B, C
        """

        #1
        fade_out_animations, move_animations = scene4.fadeOutEntries(matrixC_scene2), scene4.moveCEnteriesToCenter(matrixC_scene2)
        self.play(*fade_out_animations,
                *move_animations)
        self.wait(2)
        
        #2
        move_animations = scene4.moveMatrixCtoOriginalPosition(matrixC_scene1, matrixC_scene2)
        self.play(*move_animations)
        self.wait(1)
        
        matrixB_scene4 = scene1.createMatrixB()
        matrixA_scene4 = scene1.createMatrixA()
        
        matrices = VGroup(
            equal_sign,
            matrixB_scene4,
            multi_sign,
            matrixA_scene4
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        matrices.move_to(ORIGIN).shift(LEFT * 1.5)
        
        self.play(FadeIn(matrices))
        self.wait(3)