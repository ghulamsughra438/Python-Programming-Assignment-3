# Question No. 04
# Simple ATM Program
balance = 50000

while True:
    print("\n ATM MENU ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully.")
            print("Updated Balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
