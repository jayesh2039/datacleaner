# datacleaner/cleaner.py

import pandas as pd
import logging

class DataCleaner:
    """
    A class to clean data in a CSV file by handling NaN values and duplicates.

    Attributes:
    -----------
    file_path : str
        The path to the CSV file to be cleaned.
    df : pd.DataFrame
        The DataFrame containing the CSV data.
    drop_thresh : int
        The number of NaN values in a row to trigger its removal.
    fill_methods : list
        List of methods to use for filling NaN values.
    nan_col_thresh : float
        The threshold for the percentage of NaN values in a column to trigger its removal.

    Methods:
    --------
    clean_data():
        Cleans the data by handling NaN values and duplicates.
    save(output_path: str):
        Saves the cleaned DataFrame to a CSV file.
    summarize():
        Provides a summary of the DataFrame before and after cleaning.
    """

    def __init__(self, file_path, drop_thresh=3, fill_methods=None, nan_col_thresh=0.9):
        self.file_path = file_path
        self.drop_thresh = drop_thresh
        self.fill_methods = fill_methods if fill_methods is not None else ['ffill', 'bfill']
        self.nan_col_thresh = nan_col_thresh

        self._load_data()

    def _load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            self.original_shape = self.df.shape
            logging.info(f"Successfully loaded data from {self.file_path}")
        except FileNotFoundError as e:
            logging.error(f"File not found: {self.file_path}")
            raise e
        except pd.errors.EmptyDataError as e:
            logging.error(f"No data: {self.file_path} is empty")
            raise e
        except pd.errors.ParserError as e:
            logging.error(f"Parsing error: {self.file_path}")
            raise e
        except Exception as e:
            logging.error(f"An error occurred while loading the file: {str(e)}")
            raise e

    def clean_data(self):
        try:
            self.df.dropna(how='all', inplace=True)
            logging.debug(f"Dropped rows where all values are NaN. New shape: {self.df.shape}")

            self.df.dropna(thresh=len(self.df.columns) - self.drop_thresh + 1, inplace=True)
            logging.debug(f"Dropped rows with more than {self.drop_thresh - 1} NaN values. New shape: {self.df.shape}")

            self.df.dropna(axis=1, thresh=int((1 - self.nan_col_thresh) * len(self.df)), inplace=True)
            logging.debug(f"Dropped columns with more than {self.nan_col_thresh * 100}% NaN values. New shape: {self.df.shape}")

            for method in self.fill_methods:
                self.df.fillna(method=method, inplace=True)
                logging.debug(f"Filled NaN values using method: {method}. Remaining NaNs: {self.df.isna().sum().sum()}")

            self.df.drop_duplicates(inplace=True)
            logging.debug(f"Dropped duplicate rows. New shape: {self.df.shape}")

            logging.info("Data cleaning completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during data cleaning: {str(e)}")
            raise e

    def save(self, output_path):
        try:
            self.df.to_csv(output_path, index=False)
            logging.info(f"Successfully saved cleaned data to {output_path}")
        except Exception as e:
            logging.error(f"An error occurred while saving the file: {str(e)}")
            raise e

    def summarize(self):
        cleaned_shape = self.df.shape
        print("Data Summary:")
        print(f"Original shape: {self.original_shape}")
        print(f"Cleaned shape: {cleaned_shape}")
        print("\nMissing values before cleaning:")
        print(self.df.isna().sum().sum())
        print("\nMissing values after cleaning:")
        print(self.df.isna().sum().sum())
        print("\nData types:")
        print(self.df.dtypes)
        print("\nData head:")
        print(self.df.head())
