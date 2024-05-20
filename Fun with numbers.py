import os

number_count = 0
number_total = 0
smallest_number = 0
largest_number = 0
plot_count = 0

#current_directory = os.getcwd()
#print(f"Current working directory: {current_directory}")

def main():
    load_stats()
    exit_flag = False

    while not exit_flag:
        clear_console()
        print("Welcome to Fun With Numbers")
        print("\nChoose from the menu below:")
        print(" (A) Check number features")
        print(" (B) Plot numbers")
        print(" (C) Check overall stats")
        print("\n (X) Save and exit")

        choice = input("\nChoice: ").upper()

        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            stats()
        elif choice == "X":
            save_stats()
            exit_flag = True

def number_features():
    clear_console()
    global number_count, number_total, smallest_number, largest_number

    number = int(input("Please enter a whole number that will be checked over: "))
    clear_console()
    print(f"The features of {number} are...")
    print("\n  Positive" if number > 0 else ("  Negative" if number < 0 else "  Zero"))
    print("  Even" if number % 2 == 0 else "  Odd")

    print("  Factors are", end=" ")
    prime_count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            prime_count += 1
            print(i, end=" ")

    print("\n", " Is a prime number" if prime_count == 2 else " Is not a prime number")
    input("\nPress enter to continue...")

    if number_count == 0:
        smallest_number = number
        largest_number = number
    else:
        largest_number = max(number, largest_number)
        smallest_number = min(number, smallest_number)

    number_count += 1
    number_total += number

def plotter():
    global plot_count
    table = [[" " for _ in range(38)] for _ in range(12)]

    while True:
        try:
            clear_console()
            x_axis = int(input("Enter x axis (1-38): "))
            y_axis = int(input("Enter y axis (1-12): "))

            if 1 <= x_axis <= 38 and 1 <= y_axis <= 12:
                table[y_axis - 1][x_axis -1] = "x"
                plot_count += 1

                print_table(table)
                print(f"Coordinates plotted: {plot_count}")

                another_plot = input("Do you wish to add another coordinate (y/n)? ").lower()
                if another_plot != 'y':
                    break
            else:
                print("Invalid coordinates. Please enter valid values.")

        except ValueError:
            print("Invalid input. Please enter integers for coordinates.")

def print_table(table):
    print("\n                                                       x axis")
    print("    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ")
    print("   ------------------------------------------------------------------------------------------------------------------")
    for i, row in enumerate(table, start=1):
        print(f"{i:2}| {'  '.join(row)} |")
    print("   ------------------------------------------------------------------------------------------------------------------")    

def stats():
    clear_console()
    print("Here are your statistics of overall use")
    print(f"\n Numbers entered: {number_count}")
    print(f" Total of numbers: {number_total}")
    print(f" Average of numbers: {number_total / number_count}")
    print(f" Smallest number entered: {smallest_number}")
    print(f" Largest number entered: {largest_number}")
    print(f" Coordinates plotted: {plot_count}")
    input("\nPress enter to return to the menu...")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_stats():
    with open("stats.txt", "w", encoding="utf-8") as file:
        file.write(f"{number_count}\n")
        file.write(f"{number_total}\n")
        file.write(f"{smallest_number}\n")
        file.write(f"{largest_number}\n")
        file.write(f"{plot_count}\n")

def load_stats():
    if not os.path.exists("stats.txt"):
        return

    with open("stats.txt", "r") as file:
        global number_count, number_total, smallest_number, largest_number, plot_count
        number_count = int(file.readline())
        number_total = int(file.readline())
        smallest_number = int(file.readline())
        largest_number = int(file.readline())
        plot_count = int(file.readline())

if __name__ == "__main__":
    main()
