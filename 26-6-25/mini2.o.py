'''You're given a dataset containing gene express1on Levels across multiple timepoints.Your task is to:
Read the dataset
Calculate variance of expression per gene
Identify the top N most dynaaic genes
Plot their expression profile using matplotlib'''
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:\Users\ASUS\Downloads\Telegram Desktop\expression_data.csv') #copy the relative path from the folder having csv file
gene_ids=df["Gene_ID"]
expression_data=df.drop(column=["Gene_ID"])
variances=expression_data.var(axis=1)
N=3
top_indices=np.argsort(-variances)[:N]
top_genes=gene_ids.iloc[top_indices]
top_expr=expression_data.iloc[top_indices]
timepoints=expression_data.columns.tolist()
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(timepoints,top_expr.iloc[i],marker='o',label=top_genes.iloc[i])
plt.title(f"Top {N} Most Dynamiv Genes (by Variance)")
plt.xlabel("Timepoints")
plt.ylabel("Expression Level")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()