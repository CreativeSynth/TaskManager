import num2kr
import kr2num
import pandas as pd

df = pd.DataFrame(columns=["task_name", "index", "prompt", "answer"])

for i in range(1, 9999):
    df = df.append(
        {
            "task_name": "number_1",
            "index": i,
            "prompt": num2kr.num2kr(i, " "),
            "answer": i,
        },
        ignore_index=True,
    )

df.to_csv("number_1/number_1.csv", index=False, encoding="utf-8-sig")
