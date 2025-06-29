#You're given a dataset containing gene expression levels acr multiple timepoints. Your task is to:
#Read the dataset
#Calculate variance of expression per gene
#Identify the top N most dynamic genes
#Plot their expression profile using matplotlib


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the file path for your dataset
# This path is specific to YOUR computer.
# Make sure the 'expression_data.csv' file exists at this exact location when you run the code.
file_path = r"C:\Users\ASUS\Downloads\Telegram Desktop\expression_data.csv"

# --- 1. Read the dataset ---
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully from your specified path.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please ensure the CSV file exists at the specified path on your computer.")
    exit() # Exit if the file is not found

# Display the first few rows and information about the dataframe
print("\nFirst 5 rows of the dataset:")
print(df.head())
print("\nInformation about the dataset:")
print(df.info())
print("\nColumn names:")
print(df.columns)

# Assume the first column is the gene identifier and the rest are timepoints
# Dynamically get the gene ID column name
gene_id_column = df.columns[0]
# All columns after the first are assumed to be timepoints for expression data
expression_columns = df.columns[1:]

# Extract expression data for variance calculation
expression_data = df[expression_columns].copy()

# --- 2. Calculate variance of expression per gene ---
# Ensure expression data columns are numeric
# Attempt to convert all expression columns to numeric, coercing errors to NaN
for col in expression_data.columns:
    expression_data[col] = pd.to_numeric(expression_data[col], errors='coerce')

# Drop rows that contain any NaN values after numeric conversion.
# This handles cases where some gene rows might have non-numeric data in expression columns.
initial_rows_count = expression_data.shape[0]
expression_data = expression_data.dropna()
rows_after_dropna_count = expression_data.shape[0]

if initial_rows_count != rows_after_dropna_count:
    print(f"\nWarning: Dropped {initial_rows_count - rows_after_dropna_count} rows due to non-numeric or missing expression data.")

# Check if expression_data is empty after dropping NaNs
if expression_data.empty:
    print("\nError: No valid numeric expression data found after preprocessing.")
    print("Please ensure the CSV file contains numeric values for gene expression at timepoints.")
else:
    # Align the original dataframe with the cleaned expression_data indices
    df_filtered = df.loc[expression_data.index].copy()
    # Calculate variance for each row (gene) across the numeric timepoint columns
    df_filtered['variance'] = expression_data.var(axis=1)

    # --- 3. Identify the top N most dynamic genes ---
    N = 10 # You can change this number to display more or fewer genes

    # Adjust N if there are fewer genes than N after filtering
    if len(df_filtered) < N:
        N = len(df_filtered)
        print(f"\nNote: Dataset contains only {N} valid genes. Displaying all of them.")

    top_dynamic_genes = df_filtered.sort_values(by='variance', ascending=False).head(N)

    print(f"\nTop {N} most dynamic genes by variance:")
    print(top_dynamic_genes[[gene_id_column, 'variance']])

    # --- 4. Plot their expression profile using matplotlib ---
    plt.figure(figsize=(12, 8)) # Set figure size for better readability

    # Iterate through the top dynamic genes to plot their expression profiles
    for index, row in top_dynamic_genes.iterrows():
        gene_name = row[gene_id_column]
        # Get the expression values corresponding to the identified timepoint columns
        expression_values = row[expression_columns]

        # Plot the expression profile
        plt.plot(expression_columns, expression_values.values, label=gene_name, marker='o', linestyle='-')

    plt.xlabel('Timepoints')
    plt.ylabel('Expression Level')
    plt.title(f'Expression Profiles of Top {N} Most Dynamic Genes')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.) # Adjust legend position to avoid overlapping plot
    plt.grid(True, linestyle='--', alpha=0.7) # Add a grid for better readability
    plt.tight_layout() # Adjust layout to prevent labels/titles from being cut off

    # Save the plot to a file
    output_plot_filename = 'top_dynamic_genes_expression_profile.png'
    plt.savefig(output_plot_filename)
    print(f"\nExpression profile plot saved as '{output_plot_filename}' in the same directory as your Python script.")
    plt.show() # Display the plot