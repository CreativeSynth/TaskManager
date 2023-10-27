import pandas as pd

class DataHolder:
    def __init__(self):
        self.data = []

    def add_data(self, task_name, prompt, answer, attribute=""):
        self.data.append({
            "task_name": task_name,
            "index": len(self.data)+1,
            "prompt": prompt,
            "answer": answer,
            "attribute": attribute,
        })
    
    def reset(self):
        self.data = []

    def save_to_csv(self, csv_filename):
        df = pd.DataFrame(self.data)
        df.to_csv(csv_filename, index=False)

    def __len__(self):
        return len(self.data)