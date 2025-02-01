from src.galamsayAPI import GalamsayAPI

if __name__ == '__main__':
    api = GalamsayAPI('data/galamsay_data.xlsx', 'logs/galamsay_analysis.db')
    api.run()