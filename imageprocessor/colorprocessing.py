import cv2
import numpy as np

class ColorProcessor:
    """Classe para processamento de cores em imagens."""
    
    @staticmethod
    def adjust_saturation(image, factor):
        """Ajusta a saturação da imagem."""
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        hsv[:, :, 1] = np.clip(hsv[:, :, 1] * factor, 0, 255)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    @staticmethod
    def adjust_hue(image, factor):
        """Ajusta o matiz da imagem."""
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        hsv[:, :, 0] = np.clip(hsv[:, :, 0] + factor, 0, 179)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    @staticmethod
    def color_balance(image, r_factor=1.0, g_factor=1.0, b_factor=1.0):
        """Ajusta o balanço de cores da imagem."""
        r, g, b = cv2.split(image)
        r = np.clip(r * r_factor, 0, 255)
        g = np.clip(g * g_factor, 0, 255)
        b = np.clip(b * b_factor, 0, 255)
        return cv2.merge([r, g, b])
