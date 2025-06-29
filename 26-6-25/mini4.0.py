'''
problem statement:  given protein sequences compute the amino acid composition and display it as a pie chart
'''
import pandas as pd 
import matplotlib.pyplot as plt
from collections import Counter
#-----data-----
data = {
    "ProteinID": [f"P{i}" for i in range(1, 13)],
    "Sequence": [
        "MAGDTPLKNQV", "AAAGGTTCCSS", "MLVITGVAGGL", "WQQVVSSGGA",
        "FFTLLVVAAK", "GGGGSSSAAA", "CCDDDEEEFF", "MMNNPPQQRR",
        "KKTTSSTTGG", "VVVVAAAAFFF", "LLLIIIHHHHH", "SSSTTTGGGAA"
    ]
}
df = pd.DataFrame(data)
#--- composition ------------------------------
all_seq = "".join(df["Sequence"])
counts = Counter(all_seq) # Corrected: 'all_seq' instead of 'all seq'
labels, sizes = zip(*sorted(counts.items()))
#--- visual ------------------------------
cmap =plt.colormaps.get_cmap("tab20")
colors =[cmap(i) for i in range(len(labels))]
plt.figure(figsize=(9,9))
wedges,_, autotexts = plt.pie(
    sizes,
    labels=labels, # Add comma here
    colors=colors,
    explode=[0.05]*len(labels), # Add comma here
    startangle=140, # Add comma here
    autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(sizes))})", # Add comma here
    textprops=dict(color="black", fontsize=10)
)
plt.legend(
    wedges,
    [f"{aa}: {cnt}" for aa, cnt in counts.items()],
    title="Amino acids (count)",
    bbox_to_anchor=(1, 0.5),
    loc="center left",
    fontsize=9
)

plt.title("Amino-Acid Composition from 12 Proteins",
          fontsize=14, fontweight="bold", color="darkblue")

plt.tight_layout()
plt.show()