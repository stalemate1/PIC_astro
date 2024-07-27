# src/libraries/data_processing.py
import pandas as pd

def CSV_info(file_name, different_path=None, path=True):
    # File paths
    if path is True:
        csv_file_path = f"/home/vaibhav/Desktop/For_PIC_internship/results_scatter_csv/{file_name}"
    else:
        csv_file_path = different_path

    # Load CSV files into pandas DataFrames
    csv_file_df = pd.read_csv(csv_file_path)

    if 'kind' in csv_file_df.columns:
        csv_file_df = csv_file_df.drop(columns=['kind'])
    
    print("CSV_File:")
    print(csv_file_df.info())
    return csv_file_df, csv_file_df.columns.tolist()

def assigning_function(column_names, df):
    length = len(column_names)
    variables = []
    for i in range(length):
        variables.append(df[column_names[i]].values.reshape(-1, 1))
    return variables
