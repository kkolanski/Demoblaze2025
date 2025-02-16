import csv

class DataReader:
    @staticmethod
    def get_csv_data(filename):
        rows = []
        with open(filename, 'r') as data_file:
            reader = csv.reader(data_file)
            # Pomijam pierwszy wiersz
            next(reader, None)
            for row in reader:
                rows.append(row)
        return rows
