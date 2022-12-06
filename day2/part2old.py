points = 0

pointValues = {"X":0,"Y":3,"Z":6}

results = (("A","R","Y"),("A","P","Z"),("A","S","X"),("B","R","X"),("B","P","Y"),("B","S","Z"),("C","R","Z"),("C","P","X"),("C","S","Y"))

with open('input.txt') as file:
    for line in file:
        op,result = line.split()
        points += pointValues[result]

        r,p = 0,0
        for item in results:
            if result in item and op in item:
                if "S" in item:
                    points += 3
                    r,p = -1,-1
                    break
                elif "R" in item:
                    r += 1
                elif "P" in item:
                    p += 1
        if p > 0:
            points += 2
        elif r > 0:
            points += 1

print(points)