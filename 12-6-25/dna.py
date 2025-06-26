# Count the number of A, T, G, C in the input string

s = input("Enter the DNA sequence: ").upper()

a_count = t_count = g_count = c_count = 0

for ch in s:
    if ch == 'A':
        a_count += 1
    elif ch == 'T':
        t_count += 1
    elif ch == 'G':
        g_count += 1
    elif ch == 'C':
        c_count += 1
dict={'A':a_count,'T':t_count,'G':g_count,'C':c_count}
print(dict)
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)




#with the dictionary
#count the dna base like a pro
#write a program 
#check whether the string has only the valid bases (A,T,C,G). Count the values

dna = input("Enter DNA sequence: ").upper()
valid_bases = {'A', 'T', 'C', 'G'}

# Check for invalid bases
if not all(base in valid_bases for base in dna):
    print("Invalid DNA sequence! Only A, T, C, G are allowed.")
else:
    print("A:", dna.count('A'))
    print("T:", dna.count('T'))
    print("C:", dna.count('C'))
    print("G:", dna.count('G'))