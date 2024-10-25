from .processing import ImageProcessor
from .utils import load_image, save_image
from .filters import FilterProcessor
from .morphology import MorphologyProcessor
from .segmentation import SegmentationProcessor
from .recognition import ObjectRecognition
from .color_processing import ColorProcessor
from .histogram import HistogramProcessor

__version__ = "0.2.0"
__all__ = [
    'ImageProcessor',
    'FilterProcessor',
    'MorphologyProcessor',
    'SegmentationProcessor',
    'ObjectRecognition',
    'ColorProcessor',
    'HistogramProcessor',
    'load_image',
    'save_image'
]
