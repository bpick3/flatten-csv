# CSV Transformation Script

This Python script transforms a CSV file into a separate CSV file with specific modifications.

## Description

The script performs the following transformations on the input CSV file:

1. Creates two additional columns by flattening the ```Party``` column. The unique values in the ```Party``` column are used as column labels in the output file.
2. Removes the ```Candidate``` column from the input file.
3. Returns only one row for each unique combination of the columns ```PrecinctName```, ```Race```, ```PrecinctCode```, and ```CountyCode```.
4. Inserts the values from the ```Votes``` column under the corresponding new flattened ```Party``` columns.
5. Deletes the ```Votes``` column from the output file.

## Requirements

* Python 3.x (newest version)
* '**csv**' module (standard library)

## Usage

1. Place the input CSV file in the same directory as the script.
2. Update the ```input_filename``` and ```output_filename``` variables in the code with the appropriate file names and paths.
3. Run the script using Python: ```python3 transform_csv.py```
4. The transformed CSV file will be saved as specified by the ```output_filename``` path.

## Limitations

* The input CSV file should have the columns ```PrecinctName```, ```Race```, ```PrecinctCode```, ```Votes```, ```CountyCode```, ```Candidate```, and ```Party``` in the correct order.
* The script assumes that the input CSV file is well-formed and contains the necessary columns.

Feel free to modify and adapt the code according to your specific requirements.
