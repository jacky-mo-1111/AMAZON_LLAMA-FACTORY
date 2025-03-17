import pandas as pd

# Load the CSV file
file_path = "cwe_software.csv"
df = pd.read_csv(file_path)

# Reset the index to move CWE IDs into a column
df_reset = df.reset_index()

# Ensure the first column (CWE ID) is explicitly converted to string without dtype issues
df_reset.iloc[:, 0] = df_reset.iloc[:, 0].astype(str).copy()

# Extract the first two columns as a list of tuples
cwe_list = list(df_reset.iloc[:, :2].itertuples(index=False, name=None))

print(cwe_list[0])



