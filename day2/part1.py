"""
opponent
A = rock
B = paper
C = scissors
player
X = rock, 1
Y = paper, 2
Z = scissors, 3

loss = 0
draw = 3
win = 6
"""
points = 0

with open('input.txt') as file:
    for line in file:
        op,me = line.split()
        points += {"X":1,"Y":2,"Z":3}[me]
        
        points += {("A","X"):3,("A","Y"):6,("A","Z"):0,("B","X"):0,("B","Y"):3,("B","Z"):6,("C","X"):6,("C","Y"):0,("C","Z"):3}[op,me]

print(points)