import os
import pandas as pd

cwd = os.path.abspath('')
files = os.listdir(cwd)

combined_df = pd.DataFrame()
skipped_files = []

for file in files:
    if file.endswith('.csv'):
        try:
            current_df = pd.read_csv(file, dtype={'Voter Registration #': str})
            if not current_df.empty:  # Check if the DataFrame is not empty
                # Add leading zeros to 'Voter Registration #' column if needed
                current_df['Voter Registration #'] = current_df['Voter Registration #'].str.zfill(8)
                # Swap 'County' and 'Voter Registration #' columns
                current_df = current_df[['Voter Registration #', 'County'] + [col for col in current_df.columns if col not in ['Voter Registration #', 'County']]]
                combined_df = pd.concat([combined_df, current_df], ignore_index=True)
            else:
                skipped_files.append((file, "Empty file"))
        except pd.errors.EmptyDataError:
            skipped_files.append((file, "EmptyDataError"))

# Print the list of skipped files and reasons
print("Skipped files:")
for file, reason in skipped_files:
    print(f"File: {file}, Reason: {reason}")

combined_df.to_csv('2023_10_24_avev.csv', index=False)
