#you have given a gen expression data from a group of patients based on the value need to tell the expressenio
#<5-- under expressed
#5-15 normal
#>15 over expressed
#enter loop through 
# enter count
#user entered list
count = int(input("Enter number of samples: "))

for i in range(count):
    exp = float(input("Enter expression value: "))
    
    if exp < 5:
        print("Under-expressed")
    elif exp >= 5 and exp <= 15:
        print("Normal")
    else:
        print("Over-expressed")
##
count = int(input("Enter number of samples: "))
expressions = []

for i in range(count):
    exp = float(input("Enter expression value: "))
    expressions.append(exp)

for exp in expressions:
    if exp < 5:
        print("Under-expressed")
    elif exp >= 5 and exp <= 15:
        print("Normal")
    else:
        print("Over-expressed")
print(expressions)

