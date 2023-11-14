import os
import json
import csv

open_directory = "C:\\Users\\1253s\\Desktop\\PythonProject\\Summary_data"
write_path = "C:\\Users\\1253s\\TaskManager\\summarization\\data.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'prompt', 'answer', 'attribute'])

for filename in os.listdir(open_directory):
    text_type = os.path.join(open_directory, filename)

    for files in os.listdir(text_type + "\\2~3sent"):
        file_path = text_type + "\\2~3sent\\" + files

        with open(file_path, "rt", encoding="utf-8") as st_json:
            raw_data = json.load(st_json)

            index    = count
            original = raw_data["Meta(Refine)"]["passage"].replace('\n ', '') + "\n\n이 글을 한국어 한 문장으로 요약해줘."
            summary  = raw_data["Annotation"]["summary1"]

            try:
                writer.writerow(['summarization', index, original, summary])
                count += 1
            except:
                err_count += 1

    print(err_count)
