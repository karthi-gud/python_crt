import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming 'expression_data.csv' is in the same directory as this script.
# If not, provide the full path: e.g., 'C:/path/to/your/expression_data.csv'
df = pd.read_csv('C:/Users/ASUS/Downloads/Telegram Desktop/expression_data.csv')

# Extract Gene IDs and expression data (all columns except the first)
gene_ids = df.iloc[:, 0]
expression_data = df.iloc[:, 1:]

# Calculate variance for each gene across timepoints
variances = expression_data.var(axis=1)

# Set the number of top dynamic genes to identify (N)
N = 3 # You can change this to any number, e.g., 10

# Get the indices of the top N genes with highest variance
top_indices = np.argsort(-variances)[:N]

# Select the names and expression data for these top genes
top_genes = gene_ids.iloc[top_indices]
top_expr = expression_data.iloc[top_indices]

# Get timepoint labels from column names (e.g., T1, T2, T3)
timepoints = expression_data.columns.tolist()

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each of the top dynamic genes
for i in range(N):
    plt.plot(timepoints, top_expr.iloc[i], marker='o', label=top_genes.iloc[i])

# Add titles and labels
plt.title(f"Top {N} Most Dynamic Genes (by Variance)")
plt.xlabel("Timepoints")
plt.ylabel("Expression Level")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()

# If you want to save the plot, uncomment the line below:
# plt.savefig('simple_dynamic_genes_expression_profile.png')