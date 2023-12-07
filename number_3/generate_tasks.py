import sys
sys.path.append('../')
from data_holder import DataHolder
import numpy as np

def to_prompt(i, j):
    return f"{i}분의 {j}을 수로 바꾸어서 출력해줘"

if __name__ == '__main__':
    holder = DataHolder()

    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            holder.add_data("number_3", to_prompt(i, j), f"{j}/{i}", attribute="easy")

    datas = []
    while(len(datas) < 500):
        i = np.random.randint(10, 100)
        j = np.random.randint(10, 100)
        if (i, j) in datas or i == j:
            continue
        datas.append((i, j))
        holder.add_data("number_3", to_prompt(i, j), f"{j}/{i}", attribute="medium")
    
    
    datas = []
    while(len(datas) < 500):
        i = np.random.randint(100, 1000)
        j = np.random.randint(100, 1000)
        if (i, j) in datas or i == j:
            continue
        datas.append((i, j))
        holder.add_data("number_3", to_prompt(i, j), f"{j}/{i}", attribute="hard")


    for i in range(1, 100):
        holder.add_data("number_3", to_prompt(i, i), f"{i}/{i}", attribute="same")
    
    
    x = np.random.choice(range(100, 1000), 400, replace=False)
    x.sort()
    for i in x:
        holder.add_data("number_3", to_prompt(i, i), f"{i}/{i}", attribute="same")

    print("생성한 데이터 총 길이 = ", len(holder))
    holder.save_to_csv("number_3.csv")