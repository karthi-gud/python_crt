import pandas as pd
import matplotlib.pyplot as plt
import os

gene_data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}
gene_df = pd.DataFrame(gene_data)

gene_family_counts = gene_df['Family'].value_counts()

print("Here's how many genes are in each family:")
print(gene_family_counts)

plt.figure(figsize=(10, 7))

bars = plt.bar(gene_family_counts.index, gene_family_counts.values, color='skyblue')

plt.xlabel("Type of Gene Family")
plt.ylabel("Number of Genes Found")
plt.title("How Our Genes Are Distributed Across Different Families")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, int(height), ha='center', va='bottom')

plt.tight_layout()

chart_file_name = 'gene_family_distribution_bar_chart_human_written.png'
plt.savefig(chart_file_name)
print(f"\nYour bar chart has been saved as '{chart_file_name}'")

plt.show()