from setuptools import setup, find_packages

setup(
    name="image_processor",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'Pillow>=8.0.0',
        'opencv-python>=4.5.0',
        'scikit-image>=0.18.0',
        'scikit-learn>=0.24.0',
        'tensorflow>=2.5.0'
    ],
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Um pacote avançado para processamento de imagens",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/image-processor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
