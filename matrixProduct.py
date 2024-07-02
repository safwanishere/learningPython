rows, cols = map(int, input().split(", "))

matrix = []
for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)
    
product = 1
for row in matrix:
    for ele in row:
        print(ele, end=" ")
        product *= ele
        
print(product)