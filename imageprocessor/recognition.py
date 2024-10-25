import cv2
import numpy as np
import tensorflow as tf

class ObjectRecognition:
    """Classe para reconhecimento de objetos em imagens."""
    
    def __init__(self):
        """Inicializa o modelo de reconhecimento."""
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_faces(self, image):
        """Detecta faces na imagem."""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
    
    @staticmethod
    def detect_edges(image, threshold1=100, threshold2=200):
        """Detecta bordas usando Canny."""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.Canny(gray, threshold1, threshold2)
    
    @staticmethod
    def find_contours(image):
        """Encontra contornos na imagem."""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
