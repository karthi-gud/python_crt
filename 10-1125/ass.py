#write sa pyhon program to read a sentence from the user and print the list of wordss in the sentence 
sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)    
for ch in range (len(sentence)):
    print(ch)
    print(sentence[ch],end="") 

