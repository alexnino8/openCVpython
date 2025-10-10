# Importacion
import cv2

# abrir la cámara
vision = cv2.VideoCapture(0)

# la funcion read() permite convertir < cv2.VideoCapture 0x101e89690> en algo mas legible
print(vision.read())
