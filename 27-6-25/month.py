#write a py progrma to read a month number from the user and print the respective number of days of that particular month 

month = int(input("Enter month number (1-12): "))

if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month in [4,6,9,11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month")


