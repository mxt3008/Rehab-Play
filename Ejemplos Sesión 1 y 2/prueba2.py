# ---------------------------------------------------
# Hands/prueba2.py
# Ejemplo de detección de manos en tiempo real con MediaPipe Hands
# Marca las puntas de los dedos (pulgar, índice, medio, anular, meñique)
# ---------------------------------------------------

# ---------------------------------------------------
# Importar librerías necesarias'
# ---------------------------------------------------
import cv2                                                      # Importar OpenCV
import mediapipe as mp                                          # Importar MediaPipe Hands

# Configuración de MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils                         # Utilidades de dibujo de MediaPipe
mp_hands = mp.solutions.hands                                   # Módulo de manos de MediaPipe

# Configuración de captura de video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)                        # Use DSHOW for Windows compatibility

# Iniciar el detector de manos
with mp_hands.Hands(                                            # Cambiar de static_image_mode a False para video
    static_image_mode=False,                                    # Cambiar a False para detección en tiempo real
    max_num_hands=2,                                            # Cambiar de 1 a 2 para detectar hasta 2 manos
    min_detection_confidence=0.5) as hands:                     # Cambiar a 0.5 para mayor precisión

    while True:                                                 # Bucle para captura de video
        ret, frame = cap.read()                                 # Leer un frame del video
        if ret == False:                                        # Si no se pudo leer el frame, salir del bucle
            break                                               # Verificar si el frame se capturó correctamente

        height, width, _ = frame.shape                          # Obtener dimensiones del frame
        frame = cv2.flip(frame, 1)                              # Voltear la imagen horizontalmente
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # Convertir a RGB para MediaPipe

        results = hands.process(frame_rgb)                      # Procesar el frame con MediaPipe Hands

        if results.multi_hand_landmarks is not None:            # Si se detectan manos
            for hand_landmarks in results.multi_hand_landmarks: # Iterar sobre las manos detectadas
                mp_drawing.draw_landmarks(                      # Dibujar las landmarks de la mano
                    frame, hand_landmarks,                      # Draw landmarks and connections
                    mp_hands.HAND_CONNECTIONS,                  # Conexiones de la mano
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=3, circle_radius=3)) # Especificaciones de dibujo
                
        cv2.imshow('Frame', frame)                              # Mostrar el frame procesado
        if cv2.waitKey(1) & 0xFF == ord('q'):                   # Salir si se presiona 'q'
            break

cap.release()                                                   # Liberar la captura de video
cv2.destroyAllWindows()                                         # Cerrar todas las ventanas de OpenCV