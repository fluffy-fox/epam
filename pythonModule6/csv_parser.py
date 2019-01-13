import csv


class CsvParser(object):

    def __init__(self, filename):
        self.filename = filename

    def save_as(self, file_to_save, new_delimiter):
        with open(self.filename, newline='') as file:
            with open(file_to_save, "w", newline='') as new_file:
                read = csv.reader(file)
                write = csv.writer(new_file, delimiter=new_delimiter)
                for rows in read:
                    write.writerow(rows)

    def get_country_profit(self, country):
        profit = 0
        with open(self.filename, newline='') as file:
            read = csv.reader(file)
            for row in read:
                if row[1] == country:
                    total = float(row[13])
                    profit += total
        return profit

    def sell_over(self, category, count):
        list_sell_over = []
        with open(self.filename, newline='') as file:
            read = csv.reader(file)
            for row in read:
                if row[2] == category and int(row[8]) >= count:
                    list_sell_over.append(row[1])
        return sorted(list_sell_over)
