#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if not (isinstance(number,(int,float))): #verify if is a number
        return "The parameter given is not a number" 
    elif number % 2 == 0: #Verify if is a even number
        return "Even"
    else:
        return "Odd"