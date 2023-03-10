# https://www.linkedin.com/learning-login/share?account=2273370&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-essential-training-18764650%2Fchallenge-factorials%3Ftrk%3Dshare_video_url%26shareId%3DO9qDwjxFSC233fVRw0H0Pw%253D%253D

def factorial(number):
    if type(number) is not int: # if number is not a integer
        return None
    if number < 0: # if number is negative
        return None
    if number == 0: # if number is 0
        return 1
    if number > 0:
        fact = number  # assigning variable number to variable fact
        # Mistake code: while number <= 1:
        while number > 1: # while loop for number decrementing by one until greater than 1
            number = number - 1
            fact  = fact * number # multiply variable fact to decremented number variable and store it in fact
        return fact

print(factorial(5))
print(factorial(3))
print(factorial(-2))
print(factorial('spam spam spam spam spam'))
print(factorial(0))