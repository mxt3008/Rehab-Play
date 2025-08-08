import cv2
import numpy as np

# --- Parámetros de calibración de cámara (ajústalos según tu calibración) ---
camera_matrix = np.array([[800, 0, 320],
                          [0, 800, 240],
                          [0,   0,   1]], dtype=np.float32)

dist_coeffs = np.zeros((5, 1))  # Si no tienes distorsión, puedes dejarlo así

# --- Tamaño real del marcador en metros ---
marker_length = 0.05  # 5 cm

# --- Cargar imagen que se quiere superponer (overlay) ---
overlay_img = cv2.imread('ladrillo.png')  # Usa una imagen PNG o JPG
if overlay_img is None:
    raise ValueError("No se pudo cargar la imagen overlay.png. Asegúrate de que el archivo exista.")

overlay_height, overlay_width = overlay_img.shape[:2]

# --- Coordenadas 3D del plano (superficie del marcador) ---
object_points = np.array([
    [0, 0, 0],
    [marker_length, 0, 0],
    [marker_length, marker_length, 0],
    [0, marker_length, 0]
], dtype=np.float32)

# --- Coordenadas 2D de la imagen a superponer ---
image_points = np.array([
    [0, 0],
    [overlay_width - 1, 0],
    [overlay_width - 1, overlay_height - 1],
    [0, overlay_height - 1]
], dtype=np.float32)

# --- Inicializar detección ArUco ---
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()

# --- Abrir cámara ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("No se pudo abrir la cámara.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar marcadores ArUco
    corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        # Estimar pose de cada marcador detectado
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            rvec, tvec = rvecs[i], tvecs[i]

            # Dibujar el eje para visualizar la orientación (opcional)
            axis_length = 0.03  # 3 cm

            axis_points = np.float32([
                [0, 0, 0],             # origen
                [axis_length, 0, 0],   # eje X
                [0, axis_length, 0],   # eje Y
                [0, 0, axis_length]   # eje Z (va hacia arriba)
            ]).reshape(-1, 3)

            # Proyectar a 2D
            imgpts, _ = cv2.projectPoints(axis_points, rvec, tvec, camera_matrix, dist_coeffs)
            imgpts = imgpts.reshape(-1, 2).astype(int)

            # Dibujar ejes
            corner = tuple(imgpts[0])
            frame = cv2.line(frame, corner, tuple(imgpts[1]), (0, 0, 255), 2)  # X - rojo
            frame = cv2.line(frame, corner, tuple(imgpts[2]), (0, 255, 0), 2)  # Y - verde
            frame = cv2.line(frame, corner, tuple(imgpts[3]), (255, 0, 0), 2)  # Z - azul

            # Proyectar puntos 3D del marcador a imagen 2D
            imgpts, _ = cv2.projectPoints(object_points, rvec, tvec, camera_matrix, dist_coeffs)
            imgpts = imgpts.reshape(-1, 2).astype(np.float32)

            # Calcular la homografía entre la imagen overlay y la superficie del marcador
            H = cv2.getPerspectiveTransform(image_points, imgpts)

            # Warpear la imagen overlay para que se ajuste al marcador
            warped_overlay = cv2.warpPerspective(overlay_img, H, (frame.shape[1], frame.shape[0]))

            # Crear máscara de la región a superponer
            mask = cv2.warpPerspective(np.ones_like(overlay_img) * 255, H, (frame.shape[1], frame.shape[0]))

            # Quitar la región del marcador original
            frame_masked = cv2.bitwise_and(frame, cv2.bitwise_not(mask))
            overlay_masked = cv2.bitwise_and(warped_overlay, mask)

            # Combinar ambas
            frame = cv2.add(frame_masked, overlay_masked)

    # Mostrar frame con overlay 3D
    cv2.imshow("AR 3D Overlay", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

