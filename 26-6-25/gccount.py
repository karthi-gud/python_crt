import pandas as pd

# ----- Data provided by the user -----
data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)

# --- Function to calculate GC count for a single sequence ---
def calculate_gc_count(sequence):
    """Calculates the total count of 'G' and 'C' bases in a DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count

# --- Compute GC count for each sequence ---
df['GC_Count'] = df['Sequence'].apply(calculate_gc_count)

# --- Compute total GC count across all sequences ---
total_gc_count = df['GC_Count'].sum()

# --- Display the results (you can remove these print statements if you only need the code) ---
print("GC Count per Gene:")
print(df[['GeneID', 'Sequence', 'GC_Count']])

print(f"\nTotal GC Count across all sequences: {total_gc_count}")
#write a py to count how many genes belong to each family in from the given data and visualize using bar chart