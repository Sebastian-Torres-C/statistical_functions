#setup.py
from setuptools import setup, find_packages

setup(
    name="Stadistical Functions",
    version="0.1.0",      
    packages=find_packages(),
    
    # Información sobre el autor
    author="Sebastian Torres",
    author_email="sebastian.torres.carrasco@outlook.com",
    
    # Descripción
    description="Compilado de funciones estadísticas utilizadas en el ramo de" \
    "introduccion a la ciencia de datos (2025-02)" \
    "de la Universidad de Santiago de Chile.",
    
    # Enlace al repositorio
    url="https://github.com/Sebastian-Torres-C/statistical_functions",
    
    # Dependencias (qué necesita para funcionar)
    install_requires=[
        "math",
        "numpy",
    ],
    
    # Versión de Python requerida
    python_requires=">=3.13",
    
    # Palabras clave para buscar
    keywords="statistics",

    # Licencia
    license="MIT",
)