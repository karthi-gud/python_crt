#write a pyhthon program to declare a list and declare a tupple of word and map it to print the combined words in the tuple
# Write a Python program to declare a list and declare a tuple of words and map it to print the combined words in the tuple
n=int(input("Enter the number of words you want to input: "))
list=['chicken fry','chicken pakodi','chicken dum','chicken curry','chicken biryani','ice cream','chocolate cake','pasta','pizza','burger']
tuple=(250, 200, 300, 350, 400, 150, 100, 200, 250, 300)
i=1
while(i<=n):
    word=input("Enter a word: ")
    index=list.index(word)
    print(f"{word}-{tuple[index]}")
    i+=1


