# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    if len(numbers)<4:
        return "Debe proporcionar al menos 4 números positivos"
    
    positive_numbers = [num for num in numbers if num > 0]
    positive_numbers.sort()
    result = positive_numbers[0] + positive_numbers[1]
    return result