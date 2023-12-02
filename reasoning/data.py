import os
import json
import csv

open_file = "C:\\Users\\1253s\\Desktop\\PythonProject\\Reasoning\\klue-mrc-v1.1_dev.json"
write_path = "C:\\Users\\1253s\\Desktop\\PythonProject\\Reasoning\\data.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "w", newline = '', encoding = 'cp949'))
writer.writerow(['context', 'category', 'id', 'question_type', 'question', 'answer'])

with open(open_file, "r", encoding="utf-8") as st_json:
    raw_data = json.load(st_json)

    for paragraph in raw_data:
        for qa in paragraph['paragraphs'][0]['qas']:
            try:
                if len(qa['answers']) > 0:
                    writer.writerow([paragraph['paragraphs'][0]['context'], paragraph['news_category'], qa['guid'], qa['question_type'], qa['question'], qa['answers'][0]['text']])
                else:
                    writer.writerow([paragraph['paragraphs'][0]['context'], paragraph['news_category'], qa['guid'], qa['question_type'], qa['question'], qa['plausible_answers'][0]['text']])
                count += 1
            except:
                err_count += 1

    print("Succeed:", count, "/ Error:", err_count)