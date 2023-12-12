import num2kr
import sys
sys.path.append('../')
from data_holder import DataHolder
from tqdm import tqdm
import numpy as np


holder = DataHolder()

for i in range(1, 100):
    korean_str = num2kr.num2kr(i, " ")
    holder.add_data("number_1", f'수 {i}는 한국어로 얼마야? 다른 글자, 문장은 아무것도 대답하지 말고 정답 글자 하나만 출력해.', korean_str)

x = np.random.choice(range(100, 1000), 300, replace=False)
x.sort()
for i in x:
    korean_str = num2kr.num2kr(i, " ")
    holder.add_data("number_1", f'수 {i}는 한국어로 얼마야? 다른 글자, 문장은 아무것도 대답하지 말고 정답 글자 하나만 출력해.', korean_str)

x = np.random.choice(range(1000, 10000), 600, replace=False)
x.sort()
for i in x:
    korean_str = num2kr.num2kr(i, " ")
    holder.add_data("number_1", f'수 {i}는 한국어로 얼마야? 다른 글자, 문장은 아무것도 대답하지 말고 정답 글자 하나만 출력해.', korean_str)

holder.save_to_csv("number_1.csv")
