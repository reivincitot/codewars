# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num):
        
#    Calculates the sum of all positive integers up to a given number.

#    Args:
#        num (int): The number up to which the sum needs to be calculated.

#    Returns:
#        int: The sum of all positive integers up to the given number `num`.

#    Example:
#        result = summation(5)
#        print(result)  # Output: 15

    if num == 1:
        return num
    else:
        return num+summation(num-1)