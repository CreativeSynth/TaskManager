import csv

open_file = "C:\\Users\\1253s\\TaskManager\\translation\\사회과학\\1113_social_valid_set_151316.csv"
write_path = "C:\\Users\\1253s\\TaskManager\\translation\\사회과학\\data.csv"

count = 0
err_count = 0
writer = csv.writer(open(write_path, "wt", newline = '', encoding = 'utf8'))
writer.writerow(['task_name', 'index', 'ko', 'en', 'attribute'])

f = csv.reader(open(open_file, "rt", newline='', encoding='utf8'))

for row in f:
    if count == 0:
        count += 1
        continue

    writer.writerow(['translation/socialsci', count, row[6], row[8], row[3] + '/' + row[4] + ', ' + row[-1]])
    count += 1

print("Succeed:", count, "/ Error:", err_count)