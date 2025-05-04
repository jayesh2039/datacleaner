from datacleaner import DataCleaner

file_path = 'sample_data.csv'
output_path = 'Cleaned_Output.csv'

cleaner = DataCleaner(file_path)
cleaner.summarize()  # Before cleaning summary
cleaner.clean_data()  # Clean the data with default parameters
cleaner.summarize()  # After cleaning summary
cleaner.save(output_path)  # Save the cleaned data
