import csv
import os
import random

def random_sample(input_csv, output_csv, sample_rows_per_group):
    # Check if the input CSV file exists
    if not os.path.isfile(input_csv):
        print(f"Error: Input file '{input_csv}' not found.")
        return

    # Read all rows from the input CSV file
    with open(input_csv, 'r', encoding='utf-8', newline='') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)  # Assuming the first row is the header
        rows = list(reader)

    # Check if the sample rows per group is greater than the number of rows per group
    rows_per_group = 1000
    if sample_rows_per_group > rows_per_group:
        print(f"Error: Sample rows per group ({sample_rows_per_group}) is greater than the number of rows per group.")
        return

    # Randomly select rows from each group
    selected_rows = []
    for group_start in range(0, len(rows), rows_per_group):
        group = rows[group_start:group_start + rows_per_group]
        selected_group_rows = random.sample(group, sample_rows_per_group)
        selected_rows.extend(selected_group_rows)

    # Re-index the selected rows within each group
    for group_index, row in enumerate(selected_rows):
        row[1] = (group_index % sample_rows_per_group) + 1  # Update the index in the second column

    # Write selected rows to the output CSV file
    with open(output_csv, 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(selected_rows)

    print(f"Randomly selected {sample_rows_per_group} rows per group (with re-indexing) and written to '{output_csv}'.")

# Example usage
input_csv_file = 'translation.csv'
output_csv_file = 'translation900.csv'
sample_rows_per_group = 150  # Change this to the desired number of rows per group

random_sample(input_csv_file, output_csv_file, sample_rows_per_group)
