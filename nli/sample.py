import csv
import os
import random

def random_sample(input_csv, output_csv, sample_groups):
    # Check if the input CSV file exists
    if not os.path.isfile(input_csv):
        print(f"Error: Input file '{input_csv}' not found.")
        return

    # Read all rows from the input CSV file
    with open(input_csv, 'r', encoding='utf8', newline='') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)  # Assuming the first row is the header
        rows = list(reader)

    # Check if the sample groups is greater than the number of groups
    total_groups = len(rows) // 3
    if sample_groups > total_groups:
        print(f"Error: Sample groups ({sample_groups}) is greater than the total number of groups in the input file.")
        return

    # Randomly select groups
    selected_group_indices = random.sample(range(total_groups), sample_groups)

    # Extract rows corresponding to the selected groups
    selected_rows = []
    for group_index in selected_group_indices:
        group_start = group_index * 3
        selected_rows.extend(rows[group_start:group_start + 3])

    # Re-index the selected rows
    for index, row in enumerate(selected_rows):
        row[1] = index + 1  # Update the index in the second column

    # Write selected rows to the output CSV file
    with open(output_csv, 'w', encoding='utf8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(selected_rows)

    print(f"Randomly selected {sample_groups} groups (3 rows each) written to '{output_csv}'.")

# Example usage
input_csv_file = 'nli.csv'
output_csv_file = 'nli1000.csv'
sample_groups = 333  # Change this to the desired number of groups

random_sample(input_csv_file, output_csv_file, sample_groups)
