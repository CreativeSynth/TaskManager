import os
import json
from tqdm import tqdm
import sys
sys.path.append('../')
from data_holder import DataHolder
from hanspell import spell_checker
import time

folder_name_list = ["글짓기", "대안제시", "설명글", "주장", "찬성반대"]

def to_prompt(sentance):
    return f"내가 다음에 제공하는 문장의 맞춤법을 교정한 후 전체 문장을 [ ] 로 감싸서 출력해줘. {sentance}"

def parsing(json_data):
    sentance = json_data['essay_txt']
    sentance = sentance.replace("#@문장구분#", "")
    return sentance

def process(folder_name):
    file_list = []
    data_list = []
    try:
        file_list = os.listdir(folder_name)
    except FileNotFoundError as e:
        print(e)
        return []
    
    for file_name in tqdm(file_list):
        # 파일 확장자가 .json인 경우에만 처리합니다.
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_name, file_name)
            
            # JSON 파일을 열고 읽어들입니다.
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)
                    data_list.append(parsing(data))
                    
                except json.JSONDecodeError as e:
                    print(f"JSON 파일 {file_name}을 읽을 수 없습니다: {str(e)}")

    return data_list

if __name__ == '__main__':
    holder = DataHolder()

    for folder_name in folder_name_list:
        # read folder
        processed_list = process(folder_name)
        for data in processed_list:
            if len(data) > 450: # 너무 긴 문자는 맞춤법 검사가 불가능하므로 제외.
                continue
            holder.add_data("spelling_correct", to_prompt(data), data, attribute=folder_name)

    print("수집한 데이터 총 길이 = ", len(holder))
    holder.random_sample(1000) # Change this to the desired sample size
    print("샘플링 후 데이터 총 길이 = ", len(holder))

    for i in tqdm(range(len(holder.data))):
        prompt = holder.data[i]["answer"]
        answer = "err"
        cnt = 0
        while(cnt < 9):
            try:
                answer = spell_checker.check([prompt])[0].checked
                break
            except:
                cnt+=1
                time.sleep(0.1)
                print(f"errr on {prompt}")
        holder.data[i]["answer"] = answer

    holder.save_to_csv("spelling_correct.csv")