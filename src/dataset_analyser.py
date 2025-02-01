import pandas as pd

class DatasetAnalyser:
    def __init__(self, data):
        self.data = data

# Returns total number of Galamsay sites in the dataset file
    def calculate_total_sites(self):
        return self.data['Number_of_Galamsay_Sites'].sum()

# Finds region with highest total number of Galamsay sites
    def region_with_highest_sites(self):
        region_sites = self.data.groupby('Region')['Number_of_Galamsay_Sites'].sum()
        return region_sites.idxmax(), region_sites.max()

# Returns list of cities where number of Galamsay sites exceeds threshold inputted
    def cities_above_threshold_number(self, threshold):
        return self.data[self.data['Number_of_Galamsay_Sites'] > threshold]['City'].tolist()

# Calculates average number of Galamsay sites per region
    def average_sites_per_region(self):
        return self.data.groupby('Region')['Number_of_Galamsay_Sites'].mean()