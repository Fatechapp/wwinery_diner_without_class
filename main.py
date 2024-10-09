import random
import datetime

red_wine_stock = random.randint(1, 100)
white_wine_stock = random.randint(1, 100)

last_updated_red_wine = None
last_updated_white_wine = None

# Main loop starts here
while True:
    print("----- Main Menu -----")
    print("1. Show Menu")
    print("2. Insert Menu")
    print("3. Remove Menu")
    print("4. Exit")

    try:
        choice = int(input("Choose an option [1 - 4]: "))
    except ValueError:
        print("Invalid input. Please choose a number between 1 and 4.")
        for i in range(15):
            print("")
        continue

    if choice == 1:
        for i in range(5):
            print("")
        print("----- Show Menu -----")
        print(f"Stock of Red Wine: {red_wine_stock}")
        print(f"Stock of White Wine: {white_wine_stock}")

        if last_updated_red_wine:
            print(f"Last updated Red Wine stock: {last_updated_red_wine}")
        else:
            print("Red Wine stock has not been updated yet.")

        if last_updated_white_wine:
            print(f"Last updated White Wine stock: {last_updated_white_wine}")
        else:
            print("White Wine stock has not been updated yet.")

        for i in range(5):
            print("")

    elif choice == 2:
        for i in range(5):
            print("")
        print("----- Insert Menu -----")
        wine_type = input("Which wine do you want to update [Red | White]? ").capitalize()

        if wine_type not in ['Red', 'White']:
            print("Invalid input. Please enter 'Red' or 'White'.")
            continue

        try:
            quantity = int(input("Enter the quantity to add (greater than 10): "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if quantity <= 10:
            print("Quantity should be greater than 10.")
            continue

        if wine_type == 'Red':
            red_wine_stock += quantity
            last_updated_red_wine = datetime.datetime.now()
        else:
            white_wine_stock += quantity
            last_updated_white_wine = datetime.datetime.now()

        print(f"Successfully updated {wine_type} Wine stock!")
        for i in range(5):
            print("")

    elif choice == 3:
        for i in range(5):
            print("")
        print("----- Remove Menu -----")
        wine_type = input("Which wine do you want to remove [Red | White]? ").capitalize()

        if wine_type not in ['Red', 'White']:
            print("Invalid input. Please enter 'Red' or 'White'.")
            continue

        try:
            quantity = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if wine_type == 'Red':
            if red_wine_stock - quantity < 0:
                print("Insufficient stock. Cannot make stock negative.")
                continue
            red_wine_stock -= quantity
            last_updated_red_wine = datetime.datetime.now()
        else:
            if white_wine_stock - quantity < 0:
                print("Insufficient stock. Cannot make stock negative.")
                continue
            white_wine_stock -= quantity
            last_updated_white_wine = datetime.datetime.now()

        print(f"Successfully removed {quantity} from {wine_type} Wine stock!")
        for i in range(5):
            print("")

    elif choice == 4:
        print("Program exiting. Thank you!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 4.")
        for i in range(15):
            print("")
