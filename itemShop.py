length = int(input())
items = []

for i in range(0, length):
    items.append(int(input()))

bal = int(input())
print(f"For given input {length}", end="")
for i in items:
    print(" " + str(i), end="")
print(f" {bal},", end="")

purchaseCounter = 0
for i in items:
    if i<=bal:
        bal -= i
        purchaseCounter += 1

print(f" the output is {purchaseCounter}")

