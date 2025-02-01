from flask import Flask, jsonify
from .dataset_loader import DatasetLoader
from .dataset_cleaner import DatasetCleaner
from .dataset_analyser import DatasetAnalyser
from .db_handler import DbHandler

class GalamsayAPI:
    def __init__(self, file_path, db_path):
        self.file_path = file_path
        self.db_path = db_path
        self.app = Flask(__name__)
        self.setup_routes()

    def analyse_data(self):
        loader = DatasetLoader(self.file_path)
        data = loader.load_data_xlsx()
        cleaner = DatasetCleaner(data)
        cleaned_data = cleaner.clean_data()
        analyser = DatasetAnalyser(cleaned_data)
        results = {
            'total_sites': analyser.calculate_total_sites(),
            'highest_region': analyser.region_with_highest_sites()[0],
            'highest_sites': analyser.region_with_highest_sites()[1],
            'threshold_cities_10': analyser.cities_above_threshold_number(10),
            'threshold_cities_20': analyser.cities_above_threshold_number(20),
            'threshold_cities_35': analyser.cities_above_threshold_number(35),
            'avg_sites': analyser.average_sites_per_region().to_dict()
        }
        db_handler = DbHandler(self.db_path)
        db_handler.save_analysis_results(results)
        return results

    def setup_routes(self):
        @self.app.route('/analysis', methods=['GET'])
        def get_analysis():
            results = self.analyse_data()
            return jsonify(results)

    def run(self):
        self.app.run(debug=True)