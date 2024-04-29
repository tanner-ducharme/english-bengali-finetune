import csv
import sys

# Function to read CSV file and extract target and prediction columns
def extract_columns(csv_file, target_file, prediction_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        targets = []
        predictions = []
        for row in reader:
            targets.append(row['target'])
            predictions.append(row['prediction'])

    # Write targets to targets.txt
    with open(target_file, 'w', encoding='utf-8') as targetfile:
        for target in targets:
            targetfile.write(target + '\n')

    # Write predictions to predictions.txt
    with open(prediction_file, 'w', encoding='utf-8') as predictionfile:
        for prediction in predictions:
            predictionfile.write(prediction + '\n')

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python extract_columns.py <csv_file> <targets_output_file> <predictions_output_file>")
        sys.exit(1)

    # Extract command-line arguments
    csv_file = sys.argv[1]
    target_file = sys.argv[2]
    prediction_file = sys.argv[3]

    # Call function to extract columns
    extract_columns(csv_file, target_file, prediction_file)

