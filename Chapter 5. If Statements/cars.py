cars = ['audi', 'bmw', 'subaru', 'toyota']

# If Statement allow us to examine the state of a program and respond to it.
for car in cars:
    if car == 'bmw':  # Conditional, is the value of car equal to 'bmw'?
        print(car.upper())  # This is when the answer is True.
    else:
        print(car.title())  # Answer is no.

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
    


