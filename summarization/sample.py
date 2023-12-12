import csv
import os
import random

def random_sample(input_csv, output_csv, sample_size):
    # Check if the input CSV file exists
    if not os.path.isfile(input_csv):
        print(f"Error: Input file '{input_csv}' not found.")
        return

    # Read all rows from the input CSV file
    with open(input_csv, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)  # Assuming the first row is the header
        rows = list(reader)

    # Check if the sample size is greater than the number of rows
    if sample_size > len(rows):
        print(f"Error: Sample size ({sample_size}) is greater than the number of rows in the input file.")
        return

    # Randomly select rows
    selected_rows = random.sample(rows, sample_size)

    # Re-index the selected rows
    for index, row in enumerate(selected_rows):
        row[1] = index + 1  # Update the index in the second column

    # Write selected rows to the output CSV file
    with open(output_csv, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(selected_rows)

    print(f"Randomly selected {sample_size} rows written to '{output_csv}'.")

# Example usage
input_csv_file = 'summarization.csv'
output_csv_file = 'summarization1000.csv'
sample_size = 1000  # Change this to the desired sample size

random_sample(input_csv_file, output_csv_file, sample_size)
