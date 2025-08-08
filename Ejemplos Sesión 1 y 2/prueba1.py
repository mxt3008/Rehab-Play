# ---------------------------------------------------
# Hands/prueba1.py
# Ejemplo de detección de manos en imágenes estáticas con MediaPipe Hands
# Marca las puntas de los dedos (pulgar, índice, medio, anular, meñique)
# ---------------------------------------------------

# ---------------------------------------------------
# Importar librerías necesarias
# ---------------------------------------------------
from operator import index                                      # Importar operator (no usado en este código)
import cv2                                                      # Importar OpenCV para procesamiento de imágenes
import mediapipe as mp                                          # Importar MediaPipe para detección de manos

# Configuración de MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils                         # Utilidades de dibujo de MediaPipe
mp_hands = mp.solutions.hands                                   # Módulo de manos de MediaPipe


# Inicializar detector de manos para imágenes estáticas
with mp_hands.Hands(
    static_image_mode=True,                                     # True para imágenes estáticas (no video)
    max_num_hands=2,                                            # Detectar máximo 2 manos
    min_detection_confidence=0.5) as hands:                     # Confianza mínima del 50% para detectar manos  


    # Cargar y verificar la imagen
    image = cv2.imread("Hands/manos.jpg")                       # Cargar imagen desde archivo

    # Verificar si la imagen se cargó correctamente
    if image is None:                                           # Si la imagen no se pudo cargar
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")  # Mostrar mensaje de error
        exit()                                                  # Terminar el programa
    
    # Obtener dimensiones y procesar imagen
    height, width, _ = image.shape                              # Obtener alto, ancho y canales de la imagen

    image = cv2.flip(image, 1)                                  # Voltear imagen horizontalmente (efecto espejo)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)          # Convertir de BGR a RGB para MediaPipe

    # Procesar imagen con MediaPipe
    results = hands.process(image_rgb)                          # Detectar manos en la imagen

    # Opciones de debug (comentadas)
    #print('Handedness:', results.multi_handedness)            # Imprimir información de lateralidad (izq/der)
    #print('Hand landmarks:', results.multi_hand_landmarks)    # Imprimir coordenadas de todos los landmarks

    # Analizar resultados de detección
    if results.multi_hand_landmarks is not None:               # Si se detectaron manos

        # Definir índices de puntas de dedos
        index = [4, 8, 12, 16, 20]                             # IDs de landmarks: pulgar, índice, medio, anular, meñique

        # Procesar cada mano detectada
        for hand_landmarks in results.multi_hand_landmarks:    # Iterar sobre cada mano detectada
            
            # Opción para dibujar todos los landmarks (comentada)
            # mp_drawing.draw_landmarks(                        # Dibujar estructura completa de la mano
            #     image, hand_landmarks, mp_hands.HAND_CONNECTIONS,  # Imagen, landmarks y conexiones
            #     mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=4, circle_radius=5))  # Estilo de dibujo

            # Opción para marcar solo el dedo índice (comentada)
            # x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)  # Coordenada X del índice
            # y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height) # Coordenada Y del índice

            # Marcar puntas de todos los dedos
            for (i, points) in enumerate(hand_landmarks.landmark):  # Iterar por todos los landmarks de la mano
                if i in index:                                  # Si el landmark corresponde a una punta de dedo
                    x = int(points.x * width)                   # Convertir coordenada X normalizada a píxeles
                    y = int(points.y * height)                  # Convertir coordenada Y normalizada a píxeles
                    cv2.circle(image, (x, y), 3, (0, 255, 0), 3)  # Dibujar círculo verde en la punta del dedo

    # Opción para voltear nuevamente (comentada)
    #image = cv2.flip(image, 1)                                 # Voltear imagen verticalmente (no recomendado)

# Mostrar resultado y esperar input del usuario
cv2.imshow('Flipped Image', image)                              # Mostrar imagen procesada en ventana
cv2.waitKey(0)                                                  # Esperar hasta que se presione cualquier tecla
cv2.destroyAllWindows()                                         # Cerrar todas las ventanas de OpenCV

