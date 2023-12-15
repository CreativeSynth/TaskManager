import csv

def process(row):
    # Implement your processing logic here
    if row[2][0] == ' ': # if multiple choice question
        choices = []
        choice = ''
        flag = False
        flag2 = False

        res = ''

        row[2] = row[2][0] + '"' + row[2][1:]

        for a in row[2]:
            if flag2 == True:
                res += a
            elif flag == False and a == '"':
                flag = True
            elif flag == True and a == '"':
                choices.append(choice.strip())
                choice = ''
                flag = False
            elif flag == True:
                choice += a
            elif flag == False and a == '중':
                flag2 = True
        
        res = res.strip()
        res = res[:-10] + '는?'

        for index, choice in enumerate(choices):
            res += ' ' if index == 0 else ', '
            res += "'" + choice + "'" + '이면 ' + str(index + 1)
        
        res += '이라고 대답해.'

        row[2] = res
        row[3] = choices.index(row[3].strip()) + 1

    return row

def process_csv(input_file, output_file, encoding='utf-8'):
    with open(input_file, mode='r', encoding=encoding) as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header

        # Process each row using the provided function
        processed_rows = [process(row) for row in reader]

    with open(output_file, mode='w', encoding=encoding, newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header
        writer.writerow(header)
        
        # Write the processed rows
        writer.writerows(processed_rows)

if __name__ == "__main__":
    input_filename = 'ko_quiz_3.csv'
    output_filename = 'ko_quiz_3_edited.csv'
    
    process_csv(input_filename, output_filename)
    print(f"CSV file '{output_filename}' has been created with the modifications.")
