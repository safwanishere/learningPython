size = int(input())
array = list(map(int, input().split(", ")))

def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):      
        for j in range(i+1, n-1):          
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(f"({arr[i]}, {arr[j]}, {arr[k]})") 
                    found = True
    if (found == False): 
        print(-1)

findTriplets(array, size)