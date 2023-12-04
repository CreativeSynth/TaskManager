import pandas as pd
import re

def update_question_and_answer(row):
    if row['category'] == "알쏭달쏭 우리말":
    # Extract words inside single quotes from the question
        choices = re.findall(r"'(.*?)'", row['question'])

        # Update the question
        updated_question = row['question'] + " "
        for i, choice in enumerate(choices, start=1):
            updated_question += f"'{choice}'이 바른 말이면 {i}, "
        row['question'] = updated_question.rstrip(', ') + "라고 대답해."

        # Update the answer based on the extracted choices
        for i, choice in enumerate(choices, start=1):
            if choice in row['answer']:
                row['answer'] = i
                break
        else:
            row['answer'] = "Unknown"  # Default value if no match is found

    return row

# Load the CSV file
input_data_dir = 'korean_quiz.csv'
data = pd.read_csv(input_data_dir)

# Apply the update function to each row
new_data = data.apply(update_question_and_answer, axis=1)

# Save the modified data to a new CSV file
output_file = input_data_dir.replace('.csv', '_modified.csv')
new_data.to_csv(output_file, index=False, encoding='utf-8-sig')
