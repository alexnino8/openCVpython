import cv2

def detectar_camaras(max_index=2):
    camaras = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camaras.append(i)
            cap.release()
    return camaras

# Ejemplo de uso
camaras = detectar_camaras()
if camaras:
    print("Cámaras detectadas en los índices:", camaras)
else:
    print("No se detectaron cámaras.")