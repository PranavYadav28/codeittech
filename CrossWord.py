def make_choice(choices):
    print("Choose an option:")
    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def story_path_1():
    print("You chose path 1. This is where path 1 of the story goes.")

def story_path_2():
    print("You chose path 2. This is where path 2 of the story goes.")
  

def main():
    print("Welcome to the Interactive Story!")

    while True:
        print("\nYou find yourself at a crossroad. Which path will you choose?")
        choices = ["Path 1", "Path 2", "Quit"]
        choice = make_choice(choices)

        if choice == 1:
            story_path_1()
        elif choice == 2:
            story_path_2()
        elif choice == 3:
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()