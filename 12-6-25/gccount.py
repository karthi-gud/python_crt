dna = input("Enter DNA sequence: ").upper()
gc_count = 0

for base in dna:
    if base == 'G' or base == 'C':
        gc_count += 1

gc_percent = (gc_count / len(dna)) * 100

if gc_percent > 10:
    print("high")
else:
    print("low")

print(gc_percent)