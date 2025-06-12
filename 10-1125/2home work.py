#write a py prog to read name, contact number, mail id and password and make sure that
#contact num has only 10 dig
#mail should hava valid str following name@org_name.com 
#password should have atleast
#3 upper case alpha
#3 lower case alpha 
#3 spl charecters
#and 1 number 
#password length should not be less than 10

name = input("Enter your name: ")

contact = input("Enter your contact number: ")
if contact.isdigit() and len(contact) == 10:
    email = input("Enter your email: ")
    if "@" in email and "." in email:
        password = input("Enter your password: ")
        
        upper = 0
        lower = 0
        digit = 0
        special = 0

        for c in password:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isdigit():
                digit += 1
            elif not c.isalnum():
                special += 1

        if len(password) >= 10 and upper >= 3 and lower >= 3 and special >= 3 and digit >= 1:
            print("All inputs are valid!")
        else:
            print("Invalid password!")