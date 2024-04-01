len = int(input())
array = list(map(str,input().split()))

outputArray = []

for i in array:
    greaterCounter = 0
    for j in array:
        if int(i) < int(j):
            greaterCounter += 1
    outputArray.append(greaterCounter)

for i in outputArray:
    print(i, end=" ")