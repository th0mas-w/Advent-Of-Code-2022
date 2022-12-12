cycle = 0
x = 1

strengths = []

commands = [line.strip() for line in open("input.txt","r").readlines()]

for command in commands:

    cycle += 1
    if command == "noop":
        continue

    if cycle in [20,60,100,140,180,220]:
        print(cycle)
        strengths.append(x * cycle)

    cycle += 1

    x += int(command.split()[1])

    if cycle in [20,60,100,140,180,220]:
        print(cycle)
        strengths.append(x * cycle)


print("x:",x)
print("cycle:",cycle)

print(strengths)
print(sum(strengths))