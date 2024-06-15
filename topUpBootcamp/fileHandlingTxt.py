fp = open("topUpBootcamp/example.txt", "r")

# content = fp.read()
lineContent = fp.readlines()
lineContent[2] += "\n"
lineContent.append("lorem ispum")

print(lineContent)
fp.close()

writer = open("topUpBootcamp/example.txt", "w")
writer.writelines(lineContent)
writer.close()