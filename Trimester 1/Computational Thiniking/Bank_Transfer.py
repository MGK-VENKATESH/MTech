Valid = input("Enter the account number is valid bank account number or not?")

if Valid.lower() == "yes":
    balance = float(input("Enter balance amount"))
    amount = float(input("Enter the amount to be transfer"))
    
    if balance > amount:
        print("Transfer Successful")
        balance -= amount
        print("Remaining balance:", balance)
        
    else:
        print("Insufficient Balance")
else:
    print("InvalidBank Account Details")
