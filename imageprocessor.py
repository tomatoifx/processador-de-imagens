import cv2
import numpy as np
from scipy import ndimage

class FilterProcessor:
    """Classe para aplicação de filtros avançados em imagens."""
    
    @staticmethod
    def sobel(image, dx=1, dy=1, ksize=3):
        """
        Aplica o filtro Sobel para detecção de bordas.
        
        Args:
            image: Imagem de entrada
            dx: Ordem da derivada x
            dy: Ordem da derivada y
            ksize: Tamanho do kernel
        """
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.Sobel(gray, cv2.CV_64F, dx, dy, ksize=ksize)
    
    @staticmethod
    def laplacian(image, ksize=3):
        """
        Aplica o filtro Laplaciano para detecção de bordas.
        
        Args:
            image: Imagem de entrada
            ksize: Tamanho do kernel
        """
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    
    @staticmethod
    def unsharp_mask(image, sigma=1.0, strength=1.0):
        """
        Aplica máscara de nitidez.
        
        Args:
            image: Imagem de entrada
            sigma: Desvio padrão do filtro gaussiano
            strength: Força do efeito
        """
        blurred = ndimage.gaussian_filter(image, sigma=sigma)
        return image + strength * (image - blurred)
