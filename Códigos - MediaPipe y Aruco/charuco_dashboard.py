import os
import numpy as np
import cv2

# ------------------------------
ARUCO_DICT = cv2.aruco.DICT_6X6_250
SQUARES_VERTICALLY = 7
SQUARES_HORIZONTALLY = 5
SQUARE_LENGTH_M = 0.03  # Tamaño deseado del cuadrado negro en metros
MARKER_LENGTH_M = 0.015  # Tamaño del marcador en metros
DPI = 300  # Resolución de impresión (DPI)
MARGIN_M = 0.005  # Margen en metros
SAVE_NAME = 'ChArUco_Marker.png'
# ------------------------------

# Conversión de dimensiones de metros a píxeles
def meters_to_pixels(meters, dpi):
    return int(meters * dpi / 0.0254)

# Dimensiones en píxeles
SQUARE_LENGTH_PX = meters_to_pixels(SQUARE_LENGTH_M, DPI)
MARKER_LENGTH_PX = meters_to_pixels(MARKER_LENGTH_M, DPI)
MARGIN_PX = meters_to_pixels(MARGIN_M, DPI)

def create_and_save_new_board():
    dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
    board = cv2.aruco.CharucoBoard((SQUARES_VERTICALLY, SQUARES_HORIZONTALLY),
                                   SQUARE_LENGTH_PX, MARKER_LENGTH_PX, dictionary)
    size_ratio = SQUARES_HORIZONTALLY / SQUARES_VERTICALLY
    img = cv2.aruco.CharucoBoard.generateImage(board,
                                               (SQUARES_HORIZONTALLY * SQUARE_LENGTH_PX,
                                                int(SQUARES_VERTICALLY * SQUARE_LENGTH_PX * size_ratio)),
                                               marginSize=MARGIN_PX)
    cv2.imshow("img", img)
    cv2.waitKey(2000)
    cv2.imwrite(SAVE_NAME, img)

create_and_save_new_board()
