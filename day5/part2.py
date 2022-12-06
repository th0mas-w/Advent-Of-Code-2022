"""
[J]             [F] [M]            
[Z] [F]     [G] [Q] [F]            
[G] [P]     [H] [Z] [S] [Q]        
[V] [W] [Z] [P] [D] [G] [P]        
[T] [D] [S] [Z] [N] [W] [B] [N]    
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9 
"""

data = [["N","B","D","T","V","G","Z","J"],
        ["S","R","M","D","W","P","F"],
        ["V","C","R","S","Z"],
        ["R","T","J","Z","P","H","G"],
        ["T","C","J","N","D","Z","Q","F"],
        ["N","V","P","W","G","S","F","M"],
        ["G","C","V","B","P","Q"],
        ["Z","B","P","N"],
        ["W","P","J"]]

with open("newInput.txt") as file:
    for line in file:
        line = line.strip().split(" ")

        amount = int(line[0])
        moveFrom = int(line[2]) - 1
        moveTo = int(line[4]) - 1

        crane = data[moveFrom][len(data[moveFrom])-amount:]

        for box in crane:
            data[moveTo].append(box)
            data[moveFrom].pop()
        
for item in data:
    print(item[-1])
