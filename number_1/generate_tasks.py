import num2kr
import pandas as pd
from tqdm import tqdm

df = pd.DataFrame(columns=["task_name", "index", "prompt", "answer"])

data = []
for i in tqdm(range(1, 10000)):
    korean_str = num2kr.num2kr(i, " ")
    data.append(
        {
            "task_name": "number_1",
            "index": i,
            "prompt": f'수 {i}는 한국어로 얼마야? 다른 글자, 문장은 아무것도 대답하지 말고 정답 글자 하나만 출력해.',
            "answer": num2kr.num2kr(i, " "),
        }
    )

df = pd.concat([pd.DataFrame(data)])

df.to_csv("number_1/number_1.csv", index=False, encoding="utf-8-sig")
