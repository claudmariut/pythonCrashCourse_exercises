# The while loop, runs as long as a certain condition is True.
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# We can use the continue statement to return to the beginning of the loop.
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    # This part of the code is only read when the above condition is false.
    # Otherwise, it goes back to the beginning.
    print(number)

