# DataCleaner

DataCleaner is a Python library designed to clean data in CSV files by handling NaN values and duplicates. This library provides a convenient way to preprocess and clean your datasets for further analysis or machine learning tasks.

## Features

- Drop rows where all values are NaN.
- Drop rows with a specified number of NaN values.
- Fill NaN values with specified methods (e.g., forward fill, backward fill).
- Drop columns with a high percentage of NaN values.
- Drop duplicate rows.
- Provide a summary of the DataFrame before and after cleaning.

## Installation

You can install the `DataCleaner` library by cloning the repository and using `pip`:

```sh
git clone https://github.com/jayesh2039/datacleaner.git
cd datacleaner
pip install .
