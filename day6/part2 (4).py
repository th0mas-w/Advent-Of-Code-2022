characters = 14

fileContents = open("input.txt").read()

last14 = [item for item in fileContents[0:14]]

for char in fileContents[14:]:
    if len(set(last14)) == 14:
        break
        
    characters += 1
    last14.pop()
    last14.insert(0,char)

print(last14)
print(characters)