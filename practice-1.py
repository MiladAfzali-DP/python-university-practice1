
# -----------------------------------
# 0. Utility Functions
# -----------------------------------

def printChar(inputChar, maxChar):
  print("||", end=" ")
  print((inputChar + ' ') * maxChar, end="")
  print("||", end="\n")

def pause():
    input("\nPress Enter to return to the main menu...")


# -----------------------------------
# 1. Binary Search App
# -----------------------------------

def binarySearchApp():
    print("\n--- Binary Search App ---")

    try:
        numbers = input(
            "Enter numbers separated by commas: "
        )

        numbers = [int(item.strip()) for item in numbers.split(",")]

        target = int(input("Enter the target: "))

    except ValueError:
        print("Invalid input! Please enter integers only.")
        pause()
        return

    sorted_numbers = sorted(numbers)
    index = binarySearch(numbers, target)

    print(f"\nSorted List: {sorted_numbers}")

    if index == -1:
        print("Target not found!")

    else:
        print(f"Target found at index: {index}")

    pause()


# -----------------------------------
# 2. Shape Generator App
# -----------------------------------

def shapeGeneratorApp():
    print("\n--- Shape Generator ---")

    try:
        size = int(input("Enter the shape size: "))

        if size <= 2:
            print("Size must be greater than 2.")
            pause()
            return

    except ValueError:
        print("Invalid input! Please enter an integer.")
        pause()
        return

    # Rectangle
    print("\nRectangle:")

    for i in range(size):
      if(i == 0 or i == size - 1 or i % 3 == 0):
          printChar('—', size)
      else:
          printChar('*', size)

    # Triangle
    print("\nTriangle:")

    for i in range(size, 0, -1):
        for j in range(i):
            print(" ", end="")
        for k in range(i, size):
            if(i == size - 1):
                 print("—", end=" ")
            elif(k == i):
                print("/", end=" ")
            elif(k == size - 1):
                print("\\", end=" ")
            elif(i == 1 or i % 3 == 0):
                print("—", end=" ")
            else:
                print("*", end=" ")
        print("")

    pause()


# -----------------------------------
# 3. Collatz Conjecture App
# -----------------------------------

def collatzApp():
    print("\n--- Collatz Conjecture ---")

    try:
        number = int(input("Enter a positive integer: "))

        if number <= 0:
            print("Number must be greater than zero.")
            pause()
            return

    except ValueError:
        print("Invalid input! Please enter an integer.")
        pause()
        return

    print("\nCollatz Sequence:")

    print(number, end="")

    while number != 1:

        if number % 2 == 0:
            number = number // 2

        else:
            number = number * 3 + 1

        print(f" -> {number}", end="")

    print("\nReached 1!")
    pause()


# -----------------------------------
# 4. Hope Game
# -----------------------------------

def hopeGameApp():
    print("\n--- Hope Game ---")

    print("Choose a positive number.")
    print("Replace its multiples with 'h'.")
    print("Enter -1 anytime to exit the game.")

    try:
        chosen_number = int(input("\nEnter your number: "))

        if chosen_number <= 0:
            print("Please enter a positive number.")
            pause()
            return

    except ValueError:
        print("Invalid input! Please enter an integer.")
        pause()
        return

    current_number = 1

    print("\nGame started!")
    print("System goes first.\n")
    while True:
        # System's turn
        if current_number % chosen_number == 0:
            print(f"System: hope ({current_number})")

        else:
            print(f"System: {current_number}")

        current_number += 1

        # Calculate the expected user answer
        if current_number % chosen_number == 0:
            expected = "h"

        else:
            expected = str(current_number)

        # User's turn
        user_answer = input("Your turn: ").strip().lower()

        if user_answer == "-1":
            print("Game ended!")
            pause()
            return

        if user_answer != expected:
            print(f"Wrong answer! Correct answer: {expected}")
            print("Game over!")
            pause()
            return

        print("Correct!\n")

        current_number += 1



# -----------------------------------
# Main Menu
# -----------------------------------

def main():

    while True:

        print("\n" + "=" * 35)
        print("       Milad's MINI APPS")
        print("=" * 35)

        print("[1] Binary Search App")
        print("[2] Shape Generator")
        print("[3] Collatz Conjecture")
        print("[4] Hope Game")
        print("[0] Exit")

        print("=" * 35)

        choice = input("Select an app (0-4): ").strip()

        if choice == "1":
            binarySearchApp()

        elif choice == "2":
            shapeGeneratorApp()

        elif choice == "3":
            collatzApp()

        elif choice == "4":
            hopeGameApp()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice! Please select 0 to 4.")
            pause()


if __name__ == "__main__":
    main()
