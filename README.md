# Step-by-Step Guide for Using the DataCleaner Library

The `DataCleaner` library provides a straightforward and efficient way to clean CSV data by handling missing values and duplicates. Below is a step-by-step guide to help you understand how to use this library effectively.

Step 1: Installation
Before using the library, you need to install it. If you have cloned the repository, you can install it using `pip`.

`git clone https://github.com/jayesh2039/datacleaner.git`

`cd datacleaner`

`pip install .`

Alternatively, if the library is available on PyPI, you can install it directly from there:

`pip install datacleaner`

Step 2: Import the Library
After installation, you need to import the DataCleaner class from the library in your Python script.

`import logging`

`from datacleaner import DataCleaner`

Step 3: Set Up Logging
To monitor the library's operations, set up logging. This will help you see informative messages about the data cleaning process.

`logging.basicConfig(level=logging.INFO)`

Step 4: Initialize the `DataCleaner`

Create an instance of the DataCleaner class by providing the path to your CSV file. Optionally, you can also specify the cleaning parameters (`drop_thresh`, `fill_methods`, and `nan_col_thresh`).

`file_path = 'your_data.csv'`

`cleaner = DataCleaner(file_path)`

Step 5: Summarize the Data Before Cleaning
To understand the state of your data before cleaning, use the `summarize()` method. This will print a summary of the DataFrame, including its shape, the number of missing values, data types, and the first few rows.

`cleaner.summarize()`

Step 6: Clean the Data
Use the `clean_data()` method to perform the cleaning operations. This method will drop rows and columns based on the specified thresholds, fill NaN values, and remove duplicates.

`cleaner.clean_data()`

Step 7: Summarize the Data After Cleaning

After cleaning, summarize the data again to see the changes made during the cleaning process.

`cleaner.summarize()`

Step 8: Save the Cleaned Data

Finally, save the cleaned DataFrame to a new CSV file using the `save()` method.

`output_path = 'cleaned_data.csv'`

`cleaner.save(output_path)`

#Full Example

Here's the complete code to illustrate the steps above:

`import logging

from datacleaner import DataCleaner

logging.basicConfig(level=logging.INFO)

file_path = 'your_data.csv'

output_path = 'cleaned_data.csv'

cleaner = DataCleaner(file_path)

cleaner.summarize()

cleaner.clean_data()

cleaner.summarize()

cleaner.save(output_path)`


