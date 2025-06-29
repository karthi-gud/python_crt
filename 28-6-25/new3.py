''' ATM
'''
class InsufficientFundsError(Exception): 
    pass
balance = 10000
try:
    amount = int(input("Enter amount to Withdraw: "))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0")
    if amount > balance:
        raise InsufficientFundsError("Insufficient balance")
    balance -= amount
    print(f"Withdrawal Successful! Remaining balance: ₹{balance}")
except ValueError as ve:
    print("Invalid input:", ve)
except InsufficientFundsError as ie:
    print("Transaction failed:", ie)