seq=input("").upper()
for i in range(len(seq)):
    seq=seq.replace("T","U")
print(seq)
seq = input("Enter DNA sequence: ").upper()
rna = seq.replace("T", "U")
print(rna)