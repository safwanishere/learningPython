len = int(input())
array = list(map(str,input().split()))
print(f"for given input {len}", end="")
for i in array:
    print(" " + i, end="")

if len > 2:
    array.remove(min(array))

sum = 0
for i in array:
    sum += int(i)
    
print(f", the output is {sum}")