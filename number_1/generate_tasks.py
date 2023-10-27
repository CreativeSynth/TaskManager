import num2kr
import sys
sys.path.append('../')
from data_holder import DataHolder
from tqdm import tqdm


holder = DataHolder()

for i in tqdm(range(1, 10000)):
    korean_str = num2kr.num2kr(i, " ")
    holder.add_data("number_1", f'수 {i}는 한국어로 얼마야? 다른 글자, 문장은 아무것도 대답하지 말고 정답 글자 하나만 출력해.', korean_str)

holder.save_to_csv("number_1.csv")
