import os
import json
import csv

open_directory = "C:\\Users\\1253s\\Desktop\\PythonProject\\Translation\\인문학\\VL_en"
write_path = "C:\\Users\\1253s\\TaskManager\\Translation\\인문학\\data2.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'ko', 'en', 'attribute'])

for files in os.listdir(open_directory):
    open_file = os.path.join(open_directory, files)
    print("Open:", open_file)

    with open(open_file, "r", encoding="utf-8") as st_json:
        raw_data = json.load(st_json)

        for book in raw_data["paragraph"]:
            for sentence in book['sentences']:
                try:
                    writer.writerow(['translation/humanities', count, sentence['src_sentence'], sentence['tgt_sentence'], ])
                    count += 1
                except:
                    err_count += 1

        print("Succeed:", count, "/ Error:", err_count)