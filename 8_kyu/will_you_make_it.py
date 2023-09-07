# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Checks if it is possible to reach a gas pump based on the distance to the pump, the car's fuel efficiency (miles per gallon), and the amount of fuel left in the car.

    Args:
        distance_to_pump (int): The distance to the gas pump in miles.
        mpg (int): The car's fuel efficiency in miles per gallon.
        fuel_left (int): The amount of fuel left in the car in gallons.

    Returns:
        bool: True if it is possible to reach the gas pump with the available fuel, False otherwise.
    """
    if distance_to_pump/mpg <= fuel_left: # Divide distance_to_pump by mpg and compare if is equal to fuel_left, if it's equal return true else false
        return True
    elif mpg == 0:
        return False
    else:
        return False