import csv

with open('file.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    counter = []

    for row in reader:
        if row["<DATE>"] in ["01.10.2020", "08.10.2020", "15.10.2020", "22.10.2020", "29.10.2020"]:
            sum = sum(reader.values())
    print(f"Количество строк: {sum}")
