import os
import csv

open_directory = "C:\\Users\\1253s\\TaskManager\\Translation"

for files in os.listdir(open_directory):
    if files == 'koen.py':
        continue
    open_file = os.path.join(open_directory, files) + "\\raw_data\\data.csv"
    write_path1 = os.path.join(open_directory, files) + "\\ko-en\\data.csv"
    write_path2 = os.path.join(open_directory, files) + "\\en-ko\\data.csv"
    print("Open:", open_file)
    print("Write1:", write_path1)
    print("write2:", write_path2)

    f = csv.reader(open(open_file, "rt", newline='', encoding='utf8'))
    writer1 = csv.writer(open(write_path1, "wt", newline = '', encoding = 'utf8'))
    writer2 = csv.writer(open(write_path2, "wt", newline = '', encoding = 'utf8'))

    writer1.writerow(['task_name', 'index', 'prompt', 'answer', 'attribute'])
    writer2.writerow(['task_name', 'index', 'prompt', 'answer', 'attribute'])

    count = 0
    err_count = 0
    
    for row in f:
        try:
            if count > 0:
                writer1.writerow([row[0], row[1], '다음 문장을 영어로 번역해 줘. ' + str(row[2]), row[3], row[4] if len(row) >= 5 else ''])
                writer2.writerow([row[0], row[1], 'Translate the following sentence into Korean. ' + str(row[3]), row[2], row[4] if len(row) >= 5 else ''])
            count += 1
        except:
            print(row)
            err_count += 1
    
    print("Succeed:", count, "/ Error:", err_count)