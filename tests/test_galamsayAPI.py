import unittest
import pandas as pd
from src.dataset_loader import DatasetLoader
from src.dataset_cleaner import DatasetCleaner
from src.dataset_analyser import DatasetAnalyser
from src.db_handler import DbHandler

class TestClasses(unittest.TestCase):

    def test_load_data_csv(self):
        data = {'Region': ['Region1', 'Region2'], 'Number_of_Galamsay_Sites': [10, 20], 'City': ['City1', 'City2']}
        df = pd.DataFrame(data)
        df.to_csv('test.csv', index=False)

        loader = DatasetLoader('test.csv')
        loaded_data = loader.load_data_csv()

        self.assertEqual(loaded_data.shape[0], 2)  
        self.assertEqual(loaded_data.columns.tolist(), ['Region', 'Number_of_Galamsay_Sites', 'City'])  # Check columns

    
    def test_clean_data(self):
        sample_data = pd.DataFrame({
            'Region': ['Region1', 'Region2', 'Region3'],
            'Number_of_Galamsay_Sites': ['ten', -5, None],
            'City': ['City1', 'City2', 'City3']
        })
        
        cleaner = DatasetCleaner(sample_data)
        cleaned_data = cleaner.clean_data()

        self.assertEqual(cleaned_data.shape[0], 2) 
        self.assertTrue('Number_of_Galamsay_Sites' in cleaned_data.columns) 

    def test_analyse_data(self):
        sample_data = pd.DataFrame({
            'Region': ['Region1', 'Region2', 'Region3'],
            'Number_of_Galamsay_Sites': [10, 20, 15],
            'City': ['City1', 'City2', 'City3']
        })

        analyser = DatasetAnalyser(sample_data)

        total_sites = analyser.calculate_total_sites()
        self.assertEqual(total_sites, 45) 

        highest_region, highest_sites = analyser.region_with_highest_sites()
        self.assertEqual(highest_region, 'Region2')
        self.assertEqual(highest_sites, 20)

        cities_above_threshold = analyser.cities_above_threshold_number(10)
        self.assertEqual(cities_above_threshold, ['City2', 'City3'])

        avg_sites = analyser.average_sites_per_region()
        self.assertEqual(avg_sites['Region1'], 10)
        self.assertEqual(avg_sites['Region2'], 20)


    def test_save_analysis_results(self):
        results = {
            'total_sites': 45,
            'highest_region': 'Region2',
            'highest_sites': 20,
            'threshold_cities_10': ['City2', 'City3'],
            'threshold_cities_20': ['City2'],
            'threshold_cities_35': [],
            'avg_sites': {'Region1': 10, 'Region2': 20, 'Region3': 15}
        }

        db_handler = DbHandler('test.db')
        db_handler.save_analysis_results(results)

        self.assertTrue(True)  

if __name__ == '__main__':
    unittest.main()
