import cv2
import numpy as np

class MorphologyProcessor:
    """Classe para operações morfológicas em imagens."""
    
    @staticmethod
    def erosion(image, kernel_size=3):
        """Aplica erosão morfológica."""
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.erode(image, kernel, iterations=1)
    
    @staticmethod
    def dilation(image, kernel_size=3):
        """Aplica dilatação morfológica."""
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.dilate(image, kernel, iterations=1)
    
    @staticmethod
    def opening(image, kernel_size=3):
        """Aplica abertura morfológica (erosão seguida de dilatação)."""
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    
    @staticmethod
    def closing(image, kernel_size=3):
        """Aplica fechamento morfológico (dilatação seguida de erosão)."""
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
