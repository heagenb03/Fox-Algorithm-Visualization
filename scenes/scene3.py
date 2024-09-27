from manim import ArcBetweenPoints, MoveAlongPath, PI, RIGHT
from constants import *
from intial import *

def moveEnteriesAcrossRight(row, matrix, alingment):
    matrix_values = []
    animations = []
    
    for column in range(MATRIX_ROW_COL_CT - 1):
        intial_entry = row + (column * (MATRIX_ROW_COL_CT**2))
        final_point_entry = row + (column + 1)
        
        arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * alingment, angle=PI/2)
        animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
        matrix_values.append(matrix[intial_entry])
        
    return animations, matrix_values
    
def moveEnteriesAcrossLeft(row, matrix, alingment):
    matrix_values = []
    animations = []
    
    for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
        intial_entry = row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))
        final_point_entry = (row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))) - column
        
        arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * alingment, angle=PI/2)
        animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
        matrix_values.append(matrix[intial_entry])
        
    return animations, matrix_values

def moveEnteriesAcrossLeftAndRight(row, matrix, alingment):
    matrix_values = []
    animations = []
    
    #Columns behind intial position
    for back_column in range(row):
        intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))
        
        #Ensures that entries stop after they reach the first column
        if back_column == 0:
            final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column)) - 1
            
            arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * alingment, angle=PI/2)
        else:
            final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column))
            
            arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * alingment, angle=PI/2)
        
        animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
        matrix_values.append(matrix[intial_entry])
    
    #Columns in front of intial position
    for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
        intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + ((front_column + back_column + 1) * (MATRIX_ROW_COL_CT**2))
        final_point_entry = row + (row * (MATRIX_ROW_COL_CT + front_column)) + 1
        
        arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * alingment, angle=PI/2)
        animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
        matrix_values.append(matrix[intial_entry])
        
    return animations, matrix_values