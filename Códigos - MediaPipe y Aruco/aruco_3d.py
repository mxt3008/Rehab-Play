import cv2
import numpy as np

# Cargar el diccionario de marcadores ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()

# Cargar la imagen que quieres superponer (ejemplo: overlay.png)
overlay_img = cv2.imread('ladrillo.png')

# Verificar si la imagen se cargó correctamente
if overlay_img is None:
    raise FileNotFoundError("No se pudo cargar la imagen.")

# Asegurar que tenga 3 canales
if overlay_img.shape[2] == 4:
    overlay_img = cv2.cvtColor(overlay_img, cv2.COLOR_BGRA2BGR)

overlay_height, overlay_width = overlay_img.shape[:2]

# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección de marcadores
    corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        for corner in corners:
            # Obtener esquinas del marcador
            pts_dst = corner[0].astype(np.float32)

            # Esquinas de la imagen overlay
            pts_src = np.array([
                [0, 0],
                [overlay_width - 1, 0],
                [overlay_width - 1, overlay_height - 1],
                [0, overlay_height - 1]
            ], dtype=np.float32)

            # Homografía
            h, _ = cv2.findHomography(pts_src, pts_dst)

            # Transformar overlay
            warped_overlay = cv2.warpPerspective(overlay_img, h, (frame.shape[1], frame.shape[0]))

            # Crear máscara para superposición
            mask = np.zeros_like(frame, dtype=np.uint8)
            cv2.fillConvexPoly(mask, pts_dst.astype(int), (255, 255, 255))
            mask_inv = cv2.bitwise_not(mask)

            # Aplicar la máscara
            frame_bg = cv2.bitwise_and(frame, mask_inv)
            overlay_fg = cv2.bitwise_and(warped_overlay, mask)

            # Combinar
            frame = cv2.add(frame_bg, overlay_fg)

    # Mostrar resultado
    cv2.imshow("AR Overlay", frame)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
