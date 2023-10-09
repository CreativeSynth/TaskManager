import num2kr
import pandas as pd
from tqdm import tqdm

df = pd.DataFrame(columns=["task_name", "index", "prompt", "answer"])

data = []
for i in tqdm(range(1, 10000)):
    data.append(
        {
            "task_name": "number_2",
            "index": i,
            "prompt": f'"{num2kr.num2kr(i, " ")}"를 수로 변환해서 대답해. 다른 글자, 문장은 아무것도 대답하지 말고 정답 수 하나만 출력해.',
            "answer": i,
        }
    )

df = pd.concat([pd.DataFrame(data)])

df.to_csv("number_2/number_2.csv", index=False, encoding="utf-8-sig")