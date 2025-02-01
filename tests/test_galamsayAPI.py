import unittest
import pandas as pd
from dataset_loader import DatasetLoader
from dataset_cleaner import DatasetCleaner
from dataset_analyser import DatasetAnalyser

class TestGalamsayAnalysis(unittest.TestCase):
    def test_dataset_loader(self):
        loader = DatasetLoader('data/galamsay_data.xlsx')
        data = loader.load_data()
        self.assertIsNotNone(data)

    def test_dataset_cleaner(self):
        data = pd.DataFrame({
            'City': ['A', 'B', 'C'],
            'Region': ['X', 'Y', 'Z'],
            'Number_of_Galamsay_Sites': [10, -5, 'abc']
        })
        cleaner = DatasetCleaner(data)
        cleaned_data = cleaner.clean_data()
        self.assertEqual(len(cleaned_data), 1)

    def test_dataset_analyser(self):
        data = pd.DataFrame({
            'City': ['A', 'B', 'C'],
            'Region': ['X', 'Y', 'Z'],
            'Number_of_Galamsay_Sites': [10, 15, 20]
        })
        analyzer = DatasetAnalyser(data)
        self.assertEqual(analyzer.calculate_total_sites(), 45)

if __name__ == '__main__':
    unittest.main()