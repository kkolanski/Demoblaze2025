import csv

class DataReader:
    @staticmethod
    def get_csv_data(filename):
        rows = []
        data_file = open(filename, "r")
        reader = csv.reader(data_file)
        # Pomiń pierwszy wiersz (nagłówki)
        next(reader, None)
        for row in reader:
            rows.append(row)
        data_file.close()
        return rows
