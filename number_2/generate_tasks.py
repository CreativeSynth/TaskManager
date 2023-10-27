import num2kr
import sys
sys.path.append('../')
from data_holder import DataHolder
from tqdm import tqdm

holder = DataHolder()

for i in tqdm(range(1, 10000)):
    korean_str = num2kr.num2kr(i, " ")
    holder.add_data("number_2", f'"{num2kr.num2kr(i, " ")}"를 수로 변환해서 대답해. 다른 글자, 문장은 아무것도 대답하지 말고 정답 수 하나만 출력해.', i)

holder.save_to_csv("number_2.csv")