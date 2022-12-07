# Doesn't work :(

count = 0
directories = {"/":{"parent":None,"children":[],"files":[],"size":0}}
currentDir = "/"
i = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        part1,part2 = line.split(" ",1)
        print(line)
        print(part2)
        print(line)
        if " " in part2:  # command is cd
            part3 = part2.split(" ")[1]
            if part3 != "..": # Go into new dir
                currentDir = part3
            else: # Go back to parent dir
                currentDir = directories[currentDir]["parent"]
        elif part2 != "ls":  # program is outputting contents of directory
            if part1 == "dir":
                directories[currentDir]["children"].append(part2)
                directories[part2] = {}
                directories[part2]["parent"] = currentDir
                directories[part2]["files"] = []
                directories[part2]["children"] = []
                directories[part2]["size"] = 0
            else:
                if part2 not in directories[currentDir]["files"]:
                    directories[currentDir]["files"].append(part2)
                    directories[currentDir]["size"] += int(part1)

                    if directories[currentDir]["size"] > 100000:
                        count += 1

                    tempDir = directories[currentDir]["parent"]
                    while tempDir != None:
                        directories[tempDir]["size"] += int(part1)

                        if directories[tempDir]["size"] > 100000:
                            count += 1

                        tempDir = directories[tempDir]["parent"]
                        print(tempDir)
                        #print(directories[tempDir]["parent"])
                        

        i += 1
        if i == 50:
            break

print(directories)
print(count)