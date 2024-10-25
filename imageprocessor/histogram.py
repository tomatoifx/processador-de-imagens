import cv2
import numpy as np
import matplotlib.pyplot as plt

class HistogramProcessor:
    """Classe para processamento de histogramas."""
    
    @staticmethod
    def calculate_histogram(image, channel=None):
        """Calcula o histograma da imagem."""
        if channel is not None:
            return cv2.calcHist([image], [channel], None, [256], [0, 256])
        return [cv2.calcHist([image], [i], None, [256], [0, 256]) for i in range(3)]
    
    @staticmethod
    def equalize_histogram(image):
        """Equaliza o histograma da imagem."""
        if len(image.shape) == 2:
            return cv2.equalizeHist(image)
        else:
            ycrcb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
            ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
            return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)
    
    @staticmethod
    def plot_histogram(image, title='Histogram'):
        """Plota o histograma da imagem."""
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(hist, color=color)
        plt.title(title)
        plt.xlim([0, 256])
        plt.show()
