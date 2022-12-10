from colorama import init,Fore

init()

forest = []
visable = []
count = 0

with open("input.txt","r",encoding="UTF-8") as file:
    for row in file:
        row = row.split()[0]
        forest.append(list(row))
        visable.append([0 for i in range(len(row))])


WIDTH = len(forest[0])
HEIGHT = len(forest)

for i,row in enumerate(forest):
    for j,tree in enumerate(row):
        if j == 0 or i == 0 or j == len(forest[0]) - 1 or i == len(forest) - 1:
            visable[i][j] = 1
            continue
        
        if all(forest[i][x] < tree for x in range(j)) or all(forest[i][x] < tree for x in range(j + 1, len(forest[i]))) or all(forest[x][j] < tree for x in range(i)) or all(forest[x][i] < tree for x in range(i + 1, len(forest))):
            visable[i][j] = 1

for i in range(len(forest)):
    for j in range(len(row)):
        if visable[i][j] == 1:
            print(Fore.GREEN, forest[i][j], end="")
            count += 1
        else:
            print(Fore.RED, forest[i][j], end="")
    print()

print(count)