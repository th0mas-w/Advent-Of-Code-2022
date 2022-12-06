count = 0

with open("input.txt") as file:
    for line in file:
        item1,item2 = line[:len(line)//2],line[len(line)//2:]
        for i in range(len(item1)):
            if item1[i] in item2:
                break
        if item1[i].isupper():
            count += ord(item1[i]) - 38
        else:
            count += ord(item1[i]) - 96

print(count)