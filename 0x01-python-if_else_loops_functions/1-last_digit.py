#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    list_number = [int(x) for x in str(number)]
else:
    list_number = [int(x) for x in str(abs(number))]
    if number < 0:
        for num in range(len(list_number)):
            list_number[num] = -list_number[num]

last_number = list_number[-1:]

if last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0")
elif last_number < 6 and last_number != 0:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
