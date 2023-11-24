import os
import json
import csv

open_file = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\기술과학\\기술과학분야_한영_valid_set.json"
write_path = "C:\\Users\\1253s\\TaskManager\\translation\\기술과학\\data2.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'ko', 'en', 'attribute'])

with open(open_file, "rt", encoding="utf-8") as st_json:
    raw_data = json.load(st_json)

    for data in raw_data["data"]:
        try:
            writer.writerow(['translation/techsci', count, data['ko'], data['en'], str(data['included_unknown_words']) + ', ' + data['style']])
            count += 1
        except:
            err_count += 1

    print(err_count)