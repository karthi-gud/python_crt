# Find the reverse complement and check if it matches the original DNA sequence

seq = input("Enter DNA sequence: ").upper()

# Create complement
complement = ""
for base in seq:
    if base == 'A':
        complement += 'T'
    elif base == 'T':
        complement += 'A'
    elif base == 'C':
        complement += 'G'
    elif base == 'G':
        complement += 'C'

# Reverse the complement
rev_complement = complement[::-1]

# Check if reverse complement matches the original
print(rev_complement == seq)