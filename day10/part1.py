cycle = 0
x = 1

strengths = []

commands = [line.strip() for line in open("input.txt","r").readlines()]

for i in range(len(commands)):

    cycle += 1
    if commands[i] == "noop":
        continue

    if cycle in [20,60,100,140,180,220]:
        strengths.append(x * cycle)

    cycle += 1

    x += int(commands[i].split()[1])


print("x:",x)
print("cycle:",cycle)

print(strengths)
print(sum(strengths))