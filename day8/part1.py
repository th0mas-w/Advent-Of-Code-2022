forest = []
visable = []

with open("input.txt","r",encoding="UTF-8") as file:
    for row in file:
        row = row.split()[0]
        print(row)
        forest.append(list(row))
        visable.append([0 for i in range(len(row))])


WIDTH = len(forest[0])
HEIGHT = len(forest)

for i,row in enumerate(forest):
    for j,tree in enumerate(row):
        if visable[i][j] == 1:
            continue

