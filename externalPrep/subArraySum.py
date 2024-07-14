array = list(map(int, input().split(", ")))
size = int(input())
SubArraySum = int(input())

array.sort()

for i in range(0, len(array)-2):
    x = array[i] + array[i+1] + array[i+2]
    
    # y = SubArraySum - x
    # if array[i+2] == y:
    #     print(f"{i} {i+2}")
        
    if x == SubArraySum:
        print(f"{i} {i+1}")
        break