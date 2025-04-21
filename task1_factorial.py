
def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
user_input=input('Enter a number: ' )
number=int(user_input)
result=(factorial(number))
print("The factorial of " + str(number) + " is :" + str(result))