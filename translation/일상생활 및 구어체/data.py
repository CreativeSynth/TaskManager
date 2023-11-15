import os
import json
import csv

open_file = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\일상생활 및 구어체\\VS1\\일상생활및구어체_한영_valid_set.json"
write_path = "C:\\Users\\1253s\\TaskManager\\Translation\\일상생활 및 구어체\\data2.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'ko', 'en', 'attribute'])

with open(open_file, "r", encoding="utf-8") as st_json:
    raw_data = json.load(st_json)

    for data in raw_data["data"]:
        try:
            writer.writerow(['translation/dailylife', count, data['ko'], data['en'], str(data['included_unknown_words']) + ', ' + data['style'] + ', ' + data['domain']])
            count += 1
        except:
            err_count += 1

    print(err_count)