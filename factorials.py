def factorial(number):
    value = number # for the print statement
    fact = number  # assigning variable number to variable fact
    # Mistake code: while number <= 1:
    while number > 1: # while loop for number decrementing by one until greater than 1
        number = number - 1
        fact  = fact * number # multiply variable fact to decremented number variable and store it in fact
    print("The factorial for",value, "is", fact)

factorial(5)