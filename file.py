def process_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        print("Error: The length of the list must be a multiple of 10.")
        return None

    # Create a new list with items at positions which are a multiple of 2 or 3
    result_list = [input_list[i] for i in range(len(input_list)) if i % 2 == 0 or i % 3 == 0]

    return result_list

# Get input from the user
try:
    input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
except ValueError:
    print("Error: Please enter valid integers.")
    exit()

# Process the input list
result = process_list(input_list)

# Check if an error occurred
if result is not None:
    print("Result List:", result)
