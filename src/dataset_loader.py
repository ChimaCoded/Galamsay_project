import pandas as pd

class DatasetLoader:
    def __init__(self, file_path):
        self.file_path = file_path

#Load csv file
    def load_data_csv(self):
        try:
            data = pd.read_csv(self.file_path, encoding='utf-8')
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Csv file not found. Pls check source")
    
#Load xlsx file    
    def load_data_xlsx(self):
        try:
            data = pd.read_excel(self.file_path)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Xlsx file not found. Pls check source")
    
    