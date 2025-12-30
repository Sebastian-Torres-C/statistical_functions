#setup.py
from setuptools import setup, find_packages

setup(
    name="stadistical_functions",
    version="0.1.0",      
    packages=find_packages(),
    author="Sebastian Torres",
    author_email="sebastian.torres.carrasco@outlook.com",
    description="Compilado de funciones estadísticas utilizadas en el ramo de" \
    "introduccion a la ciencia de datos (2025-02)" \
    "de la Universidad de Santiago de Chile.",
    url="https://github.com/Sebastian-Torres-C/statistical_functions",
    install_requires=[
        "math",
        "numpy",
    ],
    python_requires=">=3.13",
    keywords="statistics",
    license="MIT",
)