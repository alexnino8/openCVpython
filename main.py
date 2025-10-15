# Importacion
import cv2

# abrir la cámara
vision = cv2.VideoCapture(0)

# la funcion read() permite convertir < cv2.VideoCapture 0x101e89690> en algo mas legible
while True:
    # checar si se ha podido capturar la imagen
    ret, frame = vision.read()
    if not ret:
        print("No se ha podido capturar la imagen")
        break
    # Esta variable condendrá la imagen capturada
    captura = frame

    # convertimos la imagen a escala de grises
    captura_byn = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)

    # cv2 tiene una funcion que automaticamente construye la imagen pixel a pixel
    cv2.imshow('Video tiempo real', clasificador_rostros) # image show -> imshow

    # Tenemos que agregar una condicion de salida
    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# suelta la camara para que otra aplicacion la pueda usar
vision.release()

# destruye todas las ventanas que se hayan creado
cv2.destroyAllWindows()
