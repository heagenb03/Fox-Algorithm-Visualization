from manim import *
from constants import *

def createBlankTextbox():
    result = VGroup()
    box = Rectangle(
        height=1,
        width=1,
        fill_color=RED_E,
        fill_opacity=0.8,
        stroke_color=WHITE
    )
    
    result.add(box)
    return result

def createBlankMatrix():
    matrix = VGroup()
    box_list = []
    for i in range(MATRIX_SIZE):
        box_list.append(createBlankTextbox())
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=MATRIX_ROW_CT, cols=MATRIX_COL_CT, buff=0.25)
    return matrix
        
class Fox(Scene):
    def construct(self):
        matrixA = createBlankMatrix()
        matrixB = createBlankMatrix()
        matrixC = createBlankMatrix()
        
        matrices = VGroup(
            matrixA,
            matrixB,
            matrixC
        ).arrange(RIGHT, buff=0.25)
        
        matrices.move_to(ORIGIN)
        
        self.play(
            FadeIn(matrices)
        )
        