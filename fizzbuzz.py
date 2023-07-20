# add your code here
#FizzBuzz Challenge. Written by Andrew Jackson
number_range = 1
while number_range <= 100:
    print(number_range, end=" ")
    number_range += 1
    if number_range % 3 == 0 and number_range % 5 == 0:
        print("FizzBuzz")
    elif number_range % 3 == 0:
        print("Fizz") 
    elif number_range % 5 == 0:
        print("Buzz")
