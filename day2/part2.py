points = 0

roundPoint = {"X":0,"Y":3,"Z":6}
choicePoint = {("A","Y"):1,("A","Z"):2,("A","X"):3,("B","X"):1,("B","Y"):2,("B","Z"):3,("C","Z"):1,("C","X"):2,("C","Y"):3}

with open('input.txt') as file:
    for line in file:
        op,result = line.split()
        points += roundPoint[result]

        points += choicePoint[(op,result)]

print(points)