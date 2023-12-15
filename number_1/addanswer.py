import csv

def num2kr2(number):
    a = ['', '', '이', '삼', '사', '오', '육', '칠', '팔', '구']

    res = ''

    if number >= 1000:
        try:
            res += a[number//1000] + '천'
        except:
            print(number)
            exit()
        number %= 1000
    
    if number >= 100:
        try:
            res += a[number//100] + '백'
        except:
            print(number)
            exit()
        number %= 100
    
    b = ['', '열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']

    if number >= 10:
        try:
            res += b[number//10]
        except:
            print(number)
            exit()
        number %= 10
    
    c = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']
    res += c[number]

    return res
    

def extract_substring(input_string, char1, char2):
    start_index = input_string.find(char1)
    end_index = input_string.find(char2, start_index + 1)

    if start_index != -1 and end_index != -1:
        result = input_string[start_index + 1:end_index]
        return result
    else:
        return None

def modify_csv(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as input_file, open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        # Read and write the header
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Process the remaining rows
        for row in csv_reader:
            value = int(extract_substring(row[2], " ", "는"))
            row[-1] = num2kr2(value)
            csv_writer.writerow(row)

# Input and output file paths
input_csv_path = 'number_1.csv'
output_csv_path = 'number_1_modified.csv'

# Call the function to modify the CSV file
modify_csv(input_csv_path, output_csv_path)
