import pandas as pd
import re

# update quiz 1
def update_one(row):
    if row['category'] == "알쏭달쏭 우리말":
    # Extract words inside single quotes from the question
        choices = re.findall(r"'(.*?)'", row['question'])

        # Update the question
        updated_question = ""
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

# update quiz 2
def update_two(row):
    if row['task_name'] == "ko_quiz_2":
        # Extract sentences between double quotes
        choices = re.findall(r'"([^"]*)"', row['prompt'])

        # Update the prompt
        updated_prompt = ""
        for i, choice in enumerate(choices, start=1):
            updated_prompt += f"'{choice}'이 맞는 띄어쓰기면 {i}, "
        row['prompt'] = updated_prompt.rstrip(', ') + "라고 대답해."

        # Update the answer based on the extracted choices
        for i, choice in enumerate(choices, start=1):
            if choice.strip() in row['answer']:
                row['answer'] = i
                break
        else:
            row['answer'] = "Unknown"  # Default value if no match is found

    return row

# update quiz 4
def update_four(row):
    if row['task_name'] == "ko_quiz_4":
        # Extract the part of the prompt
        prompt_after = row['prompt'].split('중', 1)[-1]

        # Extract words from the prompt
        choices = re.findall(r'"([^"]*)"', row['prompt'])

        # Update the prompt
        updated_prompt = prompt_after.strip() + " "
        for i, choice in enumerate(choices, start=1):
            updated_prompt += f"'{choice}'이면 {i}, "
        row['prompt'] = updated_prompt.rstrip(', ') + "라고 대답해."

        # Update the answer based on the extracted choices
        for i, choice in enumerate(choices, start=1):
            if choice.strip() == row['answer'].strip():
                row['answer'] = i
                break
        else:
            row['answer'] = "Unknown"  # Default value if no match is found

    return row

# update quiz 5
def update_five(row, quiz_no):
    if row['task_name'] == f'ko_quiz_{quiz_no}':
        # Check if 'prompt' contains double quotes
        if '"' in row['prompt']:
            # Extract the part of the prompt
            prompt_after = row['prompt'].split('중', 1)[-1]
            
            # Extract words from the prompt
            choices = re.findall(r'"([^"]*)"', row['prompt'])

            # Update the prompt
            updated_prompt = prompt_after.strip() + " "
            for i, choice in enumerate(choices, start=1):
                updated_prompt += f"'{choice}'이면 {i}, "
            row['prompt'] = updated_prompt.rstrip(', ') + "라고 대답해."

            # Update the answer based on the extracted choices
            for i, choice in enumerate(choices, start=1):
                if choice.strip() == row['answer'].strip():
                    row['answer'] = i
                    break
            else:
                row['answer'] = "Unknown"

    return row

# update quiz 6
def update_six(row):
    if row['task_name'] == "ko_quiz_6":
        # Extract words from the prompt
        choices = re.findall(r'"([^"]*)"', row['prompt'])

        # Update the prompt
        updated_prompt = ""
        for i, choice in enumerate(choices, start=1):
            updated_prompt += f"'{choice}'가 옳은 표기면 {i}, "
        row['prompt'] = updated_prompt.rstrip(', ') + "라고 대답해."

        # Update the answer based on the extracted choices
        for i, choice in enumerate(choices, start=1):
            if choice.strip() == row['answer'].strip():
                row['answer'] = i
                break
        else:
            row['answer'] = "Unknown"

    return row

# update quiz 7
def update_seven(row):
    return update_five(row, 7)

# update quiz 8
def update_eight(row):
    if row['task_name'] == "ko_quiz_8":
        # Extract the part of the prompt
        prompt_before = row['prompt'].split('"', 1)[0]

        # Extract words within double quotes from the prompt
        choices = re.findall(r'"([^"]*)"', row['prompt'])

        # Update the prompt
        updated_prompt = prompt_before
        for i, choice in enumerate(choices, start=1):
            updated_prompt += f"'{choice}'이면 {i}, "
        row['prompt'] = updated_prompt.rstrip(', ') + "라고 대답하세요."

        # Update the answer based on the extracted choices
        for i, choice in enumerate(choices, start=1):
            if choice.strip() == row['answer'].strip():
                row['answer'] = i
                break
        else:
            row['answer'] = "Unknown"

    return row

# update quiz 1 again
def update_one_again(row):
    answer_part = ''
    # Check if select2 is available and not already part of the question
    if pd.notna(row['select2']) and row['select2'] not in row['question']:
        answer_part = row['select2']
    # Check if select1 is available and not already part of the question
    elif pd.notna(row['select1']) and row['select1'] not in row['question']:
        answer_part = row['select1']

    # Modify the question if an answer part is available
    if answer_part:
        row['question'] = f"'{answer_part}'에서 {row['question']}"
    
    return row

# Load the CSV file
input_data_dir = 'ko_quiz_1.csv'  # File to be updated
data = pd.read_csv(input_data_dir)

# Apply the update function to each row
new_data = data.apply(update_one_again, axis=1) # Function matching the quiz number

# Save the modified data to a new CSV file
output_file = input_data_dir.replace('.csv', '_edit.csv')
new_data.to_csv(output_file, index=False, encoding='utf-8-sig')