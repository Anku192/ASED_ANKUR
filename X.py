def calculate_average():
    """Calculates the average of a user-inputted list of numbers."""
    try:
        # Get input from user
        user_input = input("Enter numbers separated by spaces: ")
        # Convert input string to a list of floats
        numbers = [float(x) for x in user_input.split()]
        
        # Check if list is empty to avoid division by zero
        if not numbers:
            print("No numbers entered.")
            return

        # Calculate sum and length
        total_sum = sum(numbers)
        count = len(numbers)
        average = total_sum / count
        
        print(f"Numbers entered: {count}")
        print(f"Average: {average:.2f}")

    except ValueError:
        print("Invalid input! Please enter only numbers.")

if __name__ == "__main__":
    calculate_average()
