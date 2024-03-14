def greet(name):
    print("Marhaban")
    print(f"Ana ismee {name}")
    print("Kaifa haluk?")

greet("Safwan")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(10))

sentence = "This is a sentence"
words = sentence.split()
print(words)