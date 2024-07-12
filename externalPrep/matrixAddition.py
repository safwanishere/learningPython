sizeA = int(input())
A = []
for i in range(sizeA):
    k = list(map(int, input().split(", ")))
    A.append(k)

sizeB = int(input())
B = []
for i in range(sizeB):
    k = list(map(int, input().split(", ")))
    B.append(k)

sumMatrix = [[A[i][j] + B[i][j] for i in range(sizeA)] for j in range(sizeA)]

for row in sumMatrix:
    print(*row, sep=", ")