import os
import json
import csv

open_file = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\기술과학\\기술과학분야_한영_valid_set.json"
write_path = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\기술과학\\data.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "w", newline = '', encoding = 'cp949'))
writer.writerow(['sn', 'data_set', 'domain', 'ko', 'en', 'included_unknown_words', 'style'])

with open(open_file, "r", encoding="utf-8") as st_json:
    raw_data = json.load(st_json)

    for data in raw_data["data"]:
        try:
            writer.writerow([data['sn'], data['data_set'], data['domain'], data['ko'], data['en'], data['included_unknown_words'], data['style']])
            count += 1
        except:
            err_count += 1

    print(err_count)