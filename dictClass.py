dict = {"a": 1, "b": 2, "c": 3}

print(dict)

dict["a"] = 2
print(dict)

for key in dict.keys():
    if key == "b":
        dict[key] = 5

print(dict)

for key, value in dict.items():
    if value%2 != 0:
        dict[key]+=1

print(dict)