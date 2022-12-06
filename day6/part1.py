characters = 4

fileContents = open("input.txt").read()
last4 = [fileContents[0],fileContents[1],fileContents[2],fileContents[3]]

for char in fileContents[4:]:

    if len(set(last4)) == 4:
        break
        
    characters += 1
    last4.pop()
    last4.insert(0,char)
    
    
print(last4)
print(characters)