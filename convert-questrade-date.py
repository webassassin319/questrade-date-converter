import csv
from datetime import datetime

def convert_date(date_str):
    # Convert DD-MM-YY to YYYY-MM-DD
    date_obj = datetime.strptime(date_str, '%d-%m-%y')
    return date_obj.strftime('%Y-%m-%d')

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        header = next(reader)
        writer.writerow(header)
        
        # Convert and write data
        for row in reader:
            for i in range(1, 3):  # Assuming date columns are the second and third columns
                row[i] = convert_date(row[i])
            writer.writerow(row)

if __name__ == '__main__':
    
    ## Your Input Csv file
    input_file = 'data/sample-questrade-confirmations.csv'  
    
    # Path to the output CSV file with updated dates
    output_file = 'data/sample-questrade-confirmations_updated.csv'

    main(input_file, output_file)
