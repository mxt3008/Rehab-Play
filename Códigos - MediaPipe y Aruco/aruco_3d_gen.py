import cv2
import numpy as np
from PIL import Image

# Crear diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

# ID del marcador
marker_id = 0
marker_size = 700  # Tamaño del código en píxeles (sin borde)

# Crear matriz para almacenar el marcador
marker_img = np.zeros((marker_size, marker_size), dtype=np.uint8)

# Generar el marcador directamente (sin drawMarker)
cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_img, 1)

# Convertir a BGR para agregar borde blanco
marker_img_color = cv2.cvtColor(marker_img, cv2.COLOR_GRAY2BGR)

# Añadir borde blanco alrededor (en píxeles)
borde = 100
marker_with_border = cv2.copyMakeBorder(
    marker_img_color,
    top=borde,
    bottom=borde,
    left=borde,
    right=borde,
    borderType=cv2.BORDER_CONSTANT,
    value=[255, 255, 255]  # Blanco
)

# Guardar como imagen PNG
output_path = f"aruco_marker_id{marker_id}_with_border.png"
cv2.imwrite(output_path, marker_with_border)

print(f"✅ Marcador ArUco ID {marker_id} guardado como '{output_path}' con borde blanco.")


