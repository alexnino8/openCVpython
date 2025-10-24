# Importacion
import cv2

# abrir la cámara
vision = cv2.VideoCapture(0)



# face cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

detector_de_sonrisas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


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


    cara_detectada = face_cascade.detectMultiScale(captura_byn, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    sonrisa = detector_de_sonrisas.detectMultiScale(captura, scaleFactor=1.1, minNeighbors=35, minSize=(25, 25))

    for (x, y, w, h) in cara_detectada:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #proporcion_rostro = captura_byn[y:y + h, x:x + w]




    # cv2 tiene una funcion que automaticamente construye la imagen pixel a pixel
    cv2.imshow('Video tiempo real', captura) # image show -> imshow

    # Tenemos que agregar una condicion de salida
    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# suelta la camara para que otra aplicacion la pueda usar
vision.release()

# destruye todas las ventanas que se hayan creado
cv2.destroyAllWindows()
