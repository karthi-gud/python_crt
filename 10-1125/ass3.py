#writre a mail id as input frokm the useer and print the user name and organization name 
# Write a mail id as input from the user and print the user name and organization name

'''email = input("Enter your email id: ")
username, domain = email.split('@')
organization = domain.split('.')[0]
print("User name:", username)
print("Organization name:", organization)
'''

email = input("Enter the mail: ")
parts = email.split('@')
print(f"user name: {parts[0]}")
org = parts[1]
org_parts = org.split('.')
print(f"org name: {org_parts[0]}")




email = input("Enter the mail: ")
user = ""
org = ""
found_at = False

for ch in email:
    if ch == '@':
        found_at = True
        continue
    if not found_at:
        user += ch
    elif ch != '.':
        org += ch
    else:
        break

print(f"user name: {user}")
print(f"org name: {org}")