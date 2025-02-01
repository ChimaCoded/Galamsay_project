import sqlite3

class DbHandler:
    def __init__(self, db_path):
        self.db_path = db_path

# Saves analysis results into an SQLite db table created
    def save_analysis_results(self, results):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS analysis_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total_sites INTEGER,
                    highest_region TEXT,
                    highest_sites INTEGER,
                    threshold_cities_10 TEXT,
                    threshold_cities_20 TEXT,
                    threshold_cities_35 TEXT,  -- Fixed the typo (TEST → TEXT)
                    avg_sites TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                INSERT INTO analysis_results (total_sites, highest_region, highest_sites, threshold_cities_10, threshold_cities_20, threshold_cities_35, avg_sites)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                results['total_sites'],
                results['highest_region'],
                results['highest_sites'],
                str(results['threshold_cities_10']), 
                str(results['threshold_cities_20']), 
                str(results['threshold_cities_35']),  
                str(results['avg_sites'])
            ))

            conn.commit()
        finally:
            conn.close() 
