from manim import ArcBetweenPoints, MoveAlongPath, PI, RIGHT
from constants import *
from intial import *

#Scene 3
class Scene3:
    def __init__(self):
        self.RIGHT_ALINGMENT = 0.3
    
    def moveEnteriesAcrossRight(self, row, matrix, entry):
        matrix_values = []
        move_animations = []
    
        for column in range(MATRIX_ROW_COL_CT - 1):
            final_point_entry = row + (column + 1)
            
            arcPath = ArcBetweenPoints(matrix[entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * self.RIGHT_ALINGMENT, angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[entry], arcPath))
            matrix_values.append(matrix[entry])
            
        return move_animations, matrix_values
        
    def moveEnteriesAcrossLeft(self, row, matrix):
        matrix_values = []
        move_animations = []
        
        for column in range(MATRIX_ROW_COL_CT - 1, 0, -1):
            intial_entry = row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))
            final_point_entry = (row + (row * MATRIX_ROW_COL_CT) + ((column - 1) * (MATRIX_ROW_COL_CT**2))) - column
            
            arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * self.RIGHT_ALINGMENT, angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
            matrix_values.append(matrix[intial_entry])
            
        return move_animations, matrix_values

    def moveEnteriesAcrossLeftAndRight(self, row, matrix):
        matrix_values = []
        move_animations = []
        
        #Columns behind intial position
        for back_column in range(row):
            intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + (back_column * (MATRIX_ROW_COL_CT**2))
            
            #Ensures that entries stop after they reach the first column
            if back_column == 0:
                final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column)) - 1
                
                arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * self.RIGHT_ALINGMENT, angle=PI/2)
            else:
                final_point_entry = row + (row * (MATRIX_ROW_COL_CT - back_column))
                
                arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * self.RIGHT_ALINGMENT, angle=PI/2)
            
            move_animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
            matrix_values.append(matrix[intial_entry])
        
        #Columns in front of intial position
        for front_column in range(MATRIX_ROW_COL_CT - (row + 1)):
            intial_entry = (row + (row * MATRIX_ROW_COL_CT)) + ((front_column + back_column + 1) * (MATRIX_ROW_COL_CT**2))
            final_point_entry = row + (row * (MATRIX_ROW_COL_CT + front_column)) + 1
            
            arcPath = ArcBetweenPoints(matrix[intial_entry].get_center(), matrix[final_point_entry].get_center() + RIGHT * self.RIGHT_ALINGMENT, angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[intial_entry], arcPath))
            matrix_values.append(matrix[intial_entry])
            
        return move_animations, matrix_values
    
    def moveEnteries(self, matrix, count):
        matrix_values = []
        move_animations = []
        values_moving = []
        
        for value in range(MATRIX_ROW_COL_CT):
            number = count * (MATRIX_ROW_COL_CT) + value*(MATRIX_ROW_COL_CT + 1)
            
            values_moving.append(number)
        
        print(values_moving)
        
        for row in range(MATRIX_ROW_COL_CT**2):
            values = matrix[row][1].text    
'''
row_col = 3

def getEntry(row):
    grouping = [
        [0, 1, 2], 
        [3, 4, 5],
        [6, 7, 8]
        ]
    entry = (count + row) + (row_col*row)
    print(f"g: {grouping[row][row]}")
    if entry == grouping[row][]:
        print("right")
        return entry
    else:
        print("wrong")
        entry = entry - row_col
        return entry

count = 0
while count < row_col:
    for row in range(row_col):
        intial_entry = getEntry(row)
        print(f"e: {intial_entry}")
        
    count += 1
'''