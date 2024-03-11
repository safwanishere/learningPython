numbers = [1,2,3,4,5,-5,-10,-7,8,2,-10]
names = ["Madhu", "Mohan", "Murali", "Mahi"]
mixList = [1, "Madhu", -10, 10.25, True]

print(numbers)
print(names)
print(mixList)

print(len(numbers))

numbers.append(80)
print(numbers)

numbers.insert(0, 69)
print(numbers)

numbers.remove(69)
print(numbers)

numbers.pop(-1)
print(numbers)

print(numbers[0])

print(numbers[1:4])

numbers[0:3] = [3, 2, 1]
print(numbers)

numbers.sort()
print(numbers)

print(min(numbers))
print(max(numbers))