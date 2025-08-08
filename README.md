# 🤖 Rehab-Play - Taller de Visión por Computadora

**Taller de Vacaciones PUCP 2025-2 - Python**  
*Detección de Manos, ArUco Lines y ChArUco Board con OpenCV y MediaPipe*

---

## 📋 Descripción del Proyecto

Este repositorio contiene ejemplos prácticos y ejercicios del **Taller de Visión por Computadora** enfocado en:

- 🤚 **Detección de Manos con MediaPipe**
- 🎯 **Detección de Marcadores ArUco**
- 📐 **Calibración con ChArUco Board**
- 🔄 **Aplicaciones de Rehabilitación y Realidad Aumentada**

## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.8 o superior
- Webcam (para ejemplos en tiempo real)
- Imágenes de prueba con manos

### Pasos de instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/mxt3008/Rehab-Play.git
cd Rehab-Play

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt
```
## 🛠️ Dependencias Principales

```python
opencv-python==4.8.1.78         # Procesamiento de imágenes
opencv-contrib-python==4.8.1.78 # Módulos ArUco
mediapipe==0.10.7               # Detección de manos
numpy==1.24.3                   # Operaciones matemáticas
```

### Documentación Oficial
- [MediaPipe Hands](https://mediapipe.dev/solutions/hands)
- [OpenCV ArUco](https://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html)
- [Python OpenCV Tutorial](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)

### Tutoriales Recomendados
- [Computer Vision Zone](https://www.computervision.zone/)
- [PyImageSearch](https://pyimagesearch.com/)
- [LearnOpenCV](https://learnopencv.com/)

## 🎯 Casos de Uso del Taller

### Aplicaciones de Rehabilitación
- **Fisioterapia de manos**: Seguimiento de movimientos de dedos
- **Ejercicios de coordinación**: Juegos interactivos con gestos
- **Terapia ocupacional**: Actividades de motricidad fina

### Realidad Aumentada
- **Marcadores de referencia**: Posicionamiento de objetos virtuales
- **Interacción natural**: Control por gestos de manos
- **Visualización médica**: Overlay de información en tiempo real
