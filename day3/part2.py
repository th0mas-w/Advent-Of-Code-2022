count = 0
group = []

with open("input.txt") as file:
    for line in file:
        if len(group) != 3:
            group.append(line.strip())
            continue

        common = "".join(set(group[0]).intersection(group[1]))
        common = "".join(set(common).intersection(group[2]))
        
        if common.isupper():
            print(common)
            print(group)
            count += ord(common) - 38
        else:
            count += ord(common) - 96
        
        group = [line.strip()]

print(count)