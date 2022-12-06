max = 0
currentElf = 0
with open('input.txt') as file:
    for line in file:
        if line == "\n":
            if currentElf > max:
                max = currentElf
            currentElf = 0
        else:
            currentElf += int(line)

print(max)