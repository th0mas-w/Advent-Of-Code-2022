from colorama import init,Fore

init()

forest = []
count = 0

with open("input.txt","r",encoding="UTF-8") as file:
    for row in file:
        row = row.split()[0]
        forest.append(list(row))

for i,row in enumerate(forest):
    for j,t in enumerate(row):
        if all(forest[i][x] < t for x in range(j)) or all(forest[i][x] < t for x in range(j + 1, len(forest[i]))) or all(forest[x][j] < t for x in range(i)) or all(forest[x][j] < t for x in range(i + 1, len(forest))):
            count += 1

"""
for i in range(len(forest)):
    for j in range(len(row)):
        if visable[i][j] == 1:
            print(Fore.GREEN, forest[i][j], end="")
            #count += 1
        else:
            print(Fore.RED, forest[i][j], end="")
    print()
"""

print(count)