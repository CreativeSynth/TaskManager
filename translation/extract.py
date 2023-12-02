import os
import csv
import random

open_directory = os.path.dirname(os.path.abspath(__file__))

write_path = open_directory + '/translation.csv'
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'prompt', 'answer', 'attribute'])

for files in os.listdir(open_directory):
    count = 0

    if files == 'koen.py' or files == 'extract.py' or files == 'translation.csv':
        continue
    open_file = os.path.join(open_directory, files) + "/ko-en/data.csv"

    reader = csv.reader(open(open_file, "rt", newline='', encoding='utf8'))
    next(reader)

    all_rows = list(reader)
    selected = random.sample(all_rows, 1000)

    for row in selected:
        row[1] = count
        count += 1
        writer.writerow(row)