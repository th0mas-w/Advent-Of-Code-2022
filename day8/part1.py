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
        if visable[i][j] == 1:
            continue
        if j == 0 or i == 0 or j == len(forest[0]) - 1 or i == len(forest) - 1:
            visable[i][j] = 1
            continue
        # check to the right
        failed = False
        for neighbour in row[j:]:
            if int(neighbour) > int(tree):
                failed = True
                break
        if failed == False:
            visable[i][j] = 1
            continue

        # Check to the left
        failed = False
        for neighbour in row[:j]:
            if int(neighbour) > int(tree):
                failed = True
                break
        if failed == False:
            visable[i][j] = 1
            continue

        # Check to the top
        failed = False
        for neighbour_index in range(i,0,-1):
            if int(forest[neighbour_index][j]) > int(tree):
                failed = True
                break
        if failed == False:
            visable[i][j] = 1
            continue

        # Check to the bottom
        failed = False
        for neighbour_index in range(i,len(forest)):
            if int(forest[neighbour_index][j]) > int(tree):
                failed = True
                break
        if failed == False:
            visable[i][j] = 1
            continue

for i in range(len(forest)):
    for j in range(len(row)):
        if visable[i][j] == 1:
            print(Fore.GREEN, forest[i][j], end="")
            count += 1
        else:
            print(Fore.RED, forest[i][j], end="")
    print()

print(count)