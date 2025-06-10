#you are hosting the biggest party of the year and you want to invite your friends 
#write apython program to 
#add a confirmed guests to a list
#reason a guest who cancelled
#check if a friend is on the list of guests
#sor and print the final guest list
guest_list = []
while(True):
    print("********menu********")
    print("1. Add a guest")
    print("2. Remove a guest")
    print("3. Check if a guest is on the list")
    print("4. Sort and print the guest list")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        guest_name = input("Enter the name of the guest to add: ")
        guest_list.append(guest_name)
        print(f"{guest_name} has been added to the guest list.")
    elif choice == '2':
        guest_name = input("Enter the name of the guest to remove: ")
        if guest_name in guest_list:
            guest_list.remove(guest_name)
            print(f"{guest_name} has been removed from the guest list.")
        else:
            print(f"{guest_name} is not on the guest list.")
    elif choice == '3':
        guest_name = input("Enter the name of the guest to check: ")
    
        if guest_name in guest_list:
            print(f"{guest_name} is on the guest list.")
        else:
            print(f"{guest_name} is not on the guest list.")
    elif choice == '4':
        sorted_guest_list = sorted(guest_list)
        print("Sorted Guest List:")
        for name in sorted_guest_list:
            print(name)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")  
# End of the guest management program
