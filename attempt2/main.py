from manim import VGroup, Scene, FadeIn, FadeOut, MathTex, RendererType, RIGHT, LEFT, ORIGIN
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
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            matrixC_scene3 = scene3.updateMatrixC(matrixC_scene2)
            
            self.play(FadeIn(matrixC_scene3))
            
            shift_count += 1
            
        