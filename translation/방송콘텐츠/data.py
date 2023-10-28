import os
import json
import csv

open_directory = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\방송콘텐츠"
write_path = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\방송콘텐츠\\data.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "w", newline = '', encoding = 'cp949'))
writer.writerow(['category', 'id', 'ko', 'en'])

for category in os.listdir(open_directory):
    if category[:2] != 'VL':
        continue
    print(category)
    directory = os.path.join(open_directory, category)

    for file in os.listdir(directory):
        open_file = os.path.join(directory, file)
        with open(open_file, "r", encoding="utf-8") as st_json:
            raw_data = json.load(st_json)

            try:
                writer.writerow([raw_data["대분류"], raw_data['ID'], raw_data['원문'], raw_data['최종번역문']])
                count += 1
            except:
                err_count += 1

print("Succeed:", count, "/ Error:", err_count)