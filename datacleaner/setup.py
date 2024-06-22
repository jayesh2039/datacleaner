# setup.py
from setuptools import setup, find_packages

setup(
    name="datacleaner",
    version="0.1.0",
    description="A library for cleaning data in CSV files by handling NaN values and duplicates.",
    author="Jayesh Modhvadiya",
    author_email="jayeshmodhvadiya2039@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
