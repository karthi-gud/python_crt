#write a python program as input string from the user
#1 print the count of upper case vowels
#2 print the count of lower case vowels
#3 print the count of upper case consonants
#4 print the upper case consonants

s = input("Enter the words: ")

upper_vowel_count = lower_vowel_count = upper_consonant_count = 0; upper_consonants = []

for ch in s:
    if ch.isupper() and ch in "AEIOU":
        upper_vowel_count += 1
    elif ch.islower() and ch in "aeiou":
        lower_vowel_count += 1
    elif ch.isupper() and ch.isalpha() and ch not in "AEIOU":
        upper_consonant_count += 1
        upper_consonants.append(ch)

print("Count of upper case vowels:", upper_vowel_count)
print("Count of lower case vowels:", lower_vowel_count)
print("Count of upper case consonants:", upper_consonant_count)
print("Upper case consonants:", " ".join(upper_consonants))