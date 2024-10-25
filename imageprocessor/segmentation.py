import cv2
import numpy as np
from sklearn.cluster import KMeans

class SegmentationProcessor:
    """Classe para segmentação de imagens."""
    
    @staticmethod
    def threshold(image, threshold_value=127, max_value=255):
        """Aplica thresholding simples."""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, threshold_value, max_value, cv2.THRESH_BINARY)
        return thresh
    
    @staticmethod
    def adaptive_threshold(image, max_value=255, block_size=11, C=2):
        """Aplica thresholding adaptativo."""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.adaptiveThreshold(gray, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, block_size, C)
    
    @staticmethod
    def kmeans_segmentation(image, n_clusters=3):
        """Segmenta a imagem usando K-means."""
        pixels = image.reshape((-1, 3))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(pixels)
        segments = kmeans.cluster_centers_[labels]
        return segments.reshape(image.shape)
