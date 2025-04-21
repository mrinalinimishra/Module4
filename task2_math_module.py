
import math  
user_input = input("Enter a positive number: ")
number = float(user_input)  # Convert input to a float

if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)  # Number is assumed to be in radians
    print("\nResults:")
    print("Square root:", square_root)
    print("Natural logarithm (ln):", natural_log)
    print("Sine (in radians):", sine_value)
else:
    print("Please enter a number greater than 0 for these calculations.")

