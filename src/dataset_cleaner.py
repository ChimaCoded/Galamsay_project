import pandas as pd
from word2number import w2n

class DatasetCleaner:
    def __init__(self, data):
        self.data = data

    # Converts number words to digits, converts all numbers to positive, and removes invalid records
    def clean_data(self):
        def process_number(value):
            if isinstance(value, str):
                try:
                    value = w2n.word_to_num(value)  
                except ValueError:
                    return None  
            if isinstance(value, (int, float)):
                return abs(value)  
            return None  
        
        # Apply the cleaing process and remove rows where the value is invalid number
        self.data['Number_of_Galamsay_Sites'] = self.data['Number_of_Galamsay_Sites'].apply(process_number)
        self.data = self.data.dropna(subset=['Number_of_Galamsay_Sites'])  
        return self.data
