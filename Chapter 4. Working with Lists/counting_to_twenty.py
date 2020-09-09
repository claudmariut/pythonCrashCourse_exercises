for x in range(1, 21):
    print(x)

one_million = [x for x in range(1, 1_000_001)]
print(min(one_million))
print(max(one_million))
print(sum(one_million))

odd_numbers = [x for x in range(1, 20, 2)]
for number in odd_numbers:
    print(number)

odd_numbers = []
for x in range(1, 20, 2):
    odd_numbers.append(x)
print(odd_numbers)

threes = [x for x in range(3, 31, 3)]
print(threes)

cubes = []
for x in range(1, 11):
    x = x**3
    cubes.append(x)
    print(x)

cubes = [x**3 for x in range(1, 11)]
for cube in cubes:
    print(cube)
