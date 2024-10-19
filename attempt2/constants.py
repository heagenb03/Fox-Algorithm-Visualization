from manim import WHITE, YELLOW, BLACK, RED_E

#Matrix default intialization:
MATRIX_ROW_COL_CT = 3
MATRIX_BG_COLOR = RED_E
MATRIX_BORDER_COLOR = WHITE
MATRIX_TEXT_OPACITY = 0.9

#Matrix A intialization

MATRIX_A_COLOR = WHITE
#MATRIX_A_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Self set values

#OR

MATRIX_A_NUMBERS = []
for entry in range(MATRIX_ROW_COL_CT**2): #Increment values from 1 to x
    MATRIX_A_NUMBERS.append(entry + 1)

#Matrix B intialization

MATRIX_B_COLOR = YELLOW
#MATRIX_B_NUMBERS = [9, 8, 7, 6, 5, 4, 3, 2, 1] #Self set values

#OR

MATRIX_B_NUMBERS = []
for entry in range(MATRIX_ROW_COL_CT**2, 0, -1): #Decrement values from x to 1
   MATRIX_B_NUMBERS.append(entry)


#C values intialization
C_VALUES_COLOR = BLACK

#DON"T EDIT
MATRIX_BUFFER = MATRIX_ROW_COL_CT / 36
MATRIX_FONT_SIZE = MATRIX_ROW_COL_CT * 8

