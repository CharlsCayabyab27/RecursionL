# Define the function that recursively calculates the sum of a list of numbers using a lambda function
def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return (lambda x: x[0] + recursive_sum(x[1:]))(numbers)

# Test the function
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 
