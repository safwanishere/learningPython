n = int(input())
s = int(input())
array = []
for i in range(n):
    array.append(int(input()))

sum = 0
for i in array:
    sum += i
for i in array:
    sum -= i
    if sum == s:
        output = i
        break
    else:
        sum += i
    
print(f"For given input {n} {s}", end="")
for i in array:
    print(f" {i}", end="")
print(f", the output is {output}")