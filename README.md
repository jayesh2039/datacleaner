# DataCleaner Project

## Description
DataCleaner is a Python project designed to clean, preprocess, and transform data. It handles missing values, encodes categorical data, scales numerical data, and converts the cleaned data into a PyTorch tensor for further analysis or model building.

## Features
- Handle missing values (drop or fill)
- Encode categorical features using LabelEncoder
- Scale numerical features using StandardScaler
- Convert cleaned data into PyTorch tensor
- Save cleaned data and models (encoders, scalers) to files

## Requirements
This project requires the following Python libraries:
- pandas
- scikit-learn
- torch
- pickle

To install the required libraries, you can use the following command:
```bash
pip install -r requirements.txt
