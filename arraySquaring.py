len = int(input())
array = []
for i in range(0, len):
    array.append(int(input()))

outputArray = []

for i in array:
    if i < 0:
        i*=i
    outputArray.append(i)
    print(i)

