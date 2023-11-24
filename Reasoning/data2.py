import os
import json
import csv

open_file = "C:/Users/1253s/TaskManager/Reasoning/klue-mrc-v1.1_dev.json"
write_path = "C:/Users/1253s/TaskManager/Reasoning/data2.csv"

count = 1
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'UTF8'))
writer.writerow(['task_name', 'index', 'prompt', 'answer', 'attribute'])

with open(open_file, "rt", encoding="utf-8") as st_json:
    raw_data = json.load(st_json)

    for paragraph in raw_data:
        for qa in paragraph['paragraphs'][0]['qas']:
            try:
                if len(qa['answers']) > 0:
                    #writer.writerow([paragraph['paragraphs'][0]['context'], paragraph['news_category'], qa['guid'], qa['question_type'], qa['question'], qa['answers'][0]['text']])
                    writer.writerow(['reasoning', count, paragraph['paragraphs'][0]['context'].replace("\n", " ") + ' 질문: ' + qa['question'], qa['answers'][0]['text'], qa['question_type']])
                else:
                    #writer.writerow([paragraph['paragraphs'][0]['context'], paragraph['news_category'], qa['guid'], qa['question_type'], qa['question'], qa['plausible_answers'][0]['text']])
                    writer.writerow(['reasoning', count, paragraph['paragraphs'][0]['context'].replace("\n", " ") + ' 질문: ' + qa['question'], qa['plausible_answers'][0]['text'], qa['question_type']])
                count += 1
            except:
                err_count += 1

    print("Succeed:", count, "/ Error:", err_count)