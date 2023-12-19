import os
import csv

def process_csv(input_path, output_path, result_path):
    deleted = []

    try:
        with open(input_path, 'r', encoding='utf8') as input_file, open(output_path, 'w', encoding='utf8', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # Write header to the output file
            header = next(reader)
            writer.writerow(header)

            # Process each row in the input file
            for row in reader:
                try:
                    # Attempt to convert the fourth column to an integer
                    row[3] = int(row[3])
                    # If successful, write the row to the output file
                    writer.writerow(row)
                except ValueError:
                    # If conversion fails, skip the row
                    deleted.append(row[1])

        print(f"File '{input_path}' processed successfully. Modified file saved at '{output_path}'.")

        # Find matching files in result path and delete rows based on identifier
        process_result_files(result_path, input_path, deleted)

    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_result_files(result_path, input_file_path, deleted_indices):
    try:
        # Find all directories in the result path
        directories = [d for d in os.listdir(result_path) if os.path.isdir(os.path.join(result_path, d))]

        for directory in directories:
            result_file_path = os.path.join(result_path, directory, os.path.basename(input_file_path))

            # Check if the result file exists
            if os.path.exists(result_file_path):
                # Process the result file
                process_result_file(result_file_path, deleted_indices)

    except FileNotFoundError:
        print(f"Error: Result path '{result_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_result_file(result_file_path, deleted_indices):
    try:
        with open(result_file_path, 'r', encoding='utf8') as result_file, open(result_file_path + '_modified.csv', 'w', encoding='utf8', newline='') as modified_file:
            reader = csv.reader(result_file)
            writer = csv.writer(modified_file)

            # Write header to the modified file
            header = next(reader)
            writer.writerow(header)

            # Process each row in the result file
            for row in reader:
                # Delete rows based on identifier (using row[1])
                # In this example, I'm using the value in the second column (index 1) as the identifier
                # Check if the identifier exists in the processed rows from the input file
                if row[1] not in deleted_indices:
                    writer.writerow(row)

        print(f"File '{result_file_path}' processed successfully. Modified file saved at '{result_file_path}_modified'.")

    except FileNotFoundError:
        print(f"Error: Result file '{result_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file_path = 'ko_quiz_7.csv'
output_file_path = 'ko_quiz_7_modified.csv'
result_path = '../../TaskExecutor/scoring/result'
processed_rows = process_csv(input_file_path, output_file_path, result_path)
