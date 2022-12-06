newFile = open("newInput.txt","w")

with open("input.txt") as file:
    for line in file:
        newFile.write(line.split("move")[1][1:])

newFile.close()