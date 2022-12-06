import datetime

st = datetime.datetime.now()

maxElfs = [0,0,0]
currentElf = 0
with open('input.txt') as file:
    for line in file:
        if line == "\n":
            for index in range(len(maxElfs)):
                if currentElf > maxElfs[index]:
                    if maxElfs[index] > min(maxElfs):
                        maxElfs[maxElfs.index(min(maxElfs))] = maxElfs[index]
                    maxElfs[index] = currentElf
                    break
            currentElf = 0
        else:
            currentElf += int(line)
print("Execution time:", datetime.datetime.now()-st)
#print(maxElfs)
#print(sum(maxElfs))