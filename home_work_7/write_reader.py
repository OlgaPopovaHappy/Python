import csv

def write_data(file_name):
    with open("z.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(file_name)
        writer.writerow('')

def read_data(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

if __name__ == '__main__':
    read_data("z.csv")