from anytree import Node, RenderTree
# doesn't work again
"""
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

print(udo)
Node('/Udo')
print(joe)
Node('/Udo/Dan/Joe')

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
"""

count = 0
root = Node("/",files=[],seperator=".")
parent = root
currentDir = root
with open("input.txt","r") as file:
    for line in file:
        line = line.strip()
        part1,part2 = line.split(" ",1)
        if " " in part2:  # command is cd
            part3 = part2.split(" ")[1]
            if part3 != "..": # Go into new dir
                for item in root.children:
                    if item.name == part3:
                        currentDir = item
                        print("current",currentDir)
                        break
            else: # Go back to parent dir
                print(currentDir)
                if currentDir == None:
                    print("CURRENT DIR IS NONE")
                    print(line)
                    break
                else:
                    print("backtrack works")
                currentDir = currentDir.parent
        elif part2 != "ls":  # program is outputting contents of directory
            if part1 == "dir":
                if (part2 not in currentDir.children):
                    tmp = Node(part2,parent=currentDir,files=[],seperator=".")
            else:
                if part2 not in currentDir.files:
                    currentDir.files.append([part1,part2])

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
