import unittest
import pandas as pd
import os
from datacleaner import DataCleaner

class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV file for testing
        self.test_file = 'test.csv'
        self.cleaned_file = 'cleaned_test.csv'
        data = {
            'A': [1, 2, None, 4, None],
            'B': [None, None, None, 4, 5],
            'C': [1, None, 3, None, 5],
            'D': [None, None, None, None, None]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_file, index=False)

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.cleaned_file):
            os.remove(self.cleaned_file)

    def test_load_data(self):
        cleaner = DataCleaner(self.test_file)
        self.assertEqual(cleaner.df.shape, (5, 4))
        self.assertEqual(cleaner.original_shape, (5, 4))

    def test_clean_data(self):
        cleaner = DataCleaner(self.test_file, drop_thresh=2, nan_col_thresh=0.6)
        cleaner.clean_data()
        # Check if rows with 2 or more NaN values are dropped
        self.assertEqual(cleaner.df.shape[0], 3)
        # Check if columns with more than 60% NaN values are dropped
        self.assertEqual(cleaner.df.shape[1], 3)
        # Check remaining NaN values are filled
        self.assertEqual(cleaner.df.isna().sum().sum(), 0)
        # Check if duplicates are dropped
        cleaner.df = cleaner.df.append(cleaner.df.iloc[0])
        self.assertEqual(cleaner.df.duplicated().sum(), 1)
        cleaner.clean_data()
        self.assertEqual(cleaner.df.duplicated().sum(), 0)

    def test_save(self):
        cleaner = DataCleaner(self.test_file)
        cleaner.clean_data()
        cleaner.save(self.cleaned_file)
        self.assertTrue(os.path.exists(self.cleaned_file))
        saved_df = pd.read_csv(self.cleaned_file)
        self.assertEqual(saved_df.shape, cleaner.df.shape)

    def test_summarize(self):
        cleaner = DataCleaner(self.test_file)
        with self.assertLogs(level='INFO') as log:
            cleaner.summarize()
            self.assertIn('Original shape:', log.output[0])
            self.assertIn('Cleaned shape:', log.output[0])

if __name__ == '__main__':
    unittest.main()
