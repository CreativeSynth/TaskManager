import os
import json
import csv

open_directory = "C:\\Users\\1253s\\Desktop\\PythonProject\\Summary_data"
write_path = "C:\\Users\\1253s\\Desktop\\PythonProject\\summary_data.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "w", newline = '', encoding = 'cp949'))
writer.writerow(['file_id', 'index', 'query', 'answer'])

for filename in os.listdir(open_directory):
    text_type = os.path.join(open_directory, filename)

    for files in os.listdir(text_type + "\\2~3sent"):
        file_path = text_type + "\\2~3sent\\" + files

        with open(file_path, "r", encoding="utf-8") as st_json:
            raw_data = json.load(st_json)

            file_id  = file_path[len(open_directory):]
            index    = count
            original = raw_data["Meta(Refine)"]["passage"].replace('\n ', '') + "\n\n이 글을 한국어 한 문장으로 요약해줘."
            summary  = raw_data["Annotation"]["summary1"]

            try:
                writer.writerow([file_id, index, original, summary])
                count += 1
            except:
                err_count += 1

    print(err_count)
