import csv

def transform_csv(input_file, output_file):
    # Dictionary to store transformed data
    transformed_data = {}

    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Extracting relevant columns
            precinct_name = row['PrecinctName']
            race = row['Race']
            precinct_code = row['PrecinctCode']
            county_code = row['CountyCode']
            party = row['Party']
            votes = row['Votes']
            
            # Flattening 'Party' column
            if (precinct_name, race, precinct_code, county_code) not in transformed_data:
                transformed_data[(precinct_name, race, precinct_code, county_code)] = {}
                
            transformed_data[(precinct_name, race, precinct_code, county_code)][party] = int(votes)

    # Writing transformed data to output CSV file
    fieldnames = ['PrecinctName', 'Race', 'PrecinctCode', 'CountyCode'] + list(set(party for d in transformed_data.values() for party in d.keys()))
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)

        for key, party_votes in transformed_data.items():
            row = list(key) + [party_votes.get(party, 0) for party in fieldnames[4:]]
            writer.writerow(row)

    print(f"The CSV file '{input_file}' has been transformed and saved as '{output_file}'.")

# Example usage
input_filename = 'input.csv'  # Replace with the path to your input CSV file
output_filename = 'output_transformed.csv'  # Replace with the desired path for the output transformed CSV file
transform_csv(input_filename, output_filename)
