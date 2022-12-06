count = 0

with open('input.txt') as file:
    for line in file:
        as1,as2 = line.split(",")
        as2 = as2.strip()
        as1 = as1.split("-")
        as2 = as2.split("-")

        as1[0],as1[1],as2[0],as2[1] = [int(i) for i in [as1[0], as1[1], as2[0], as2[1] ]]
        
        if (as1[1] >= as2[1] and as1[0] <= as2[0]) or (as1[1] <= as2[1] and as1[0] >= as2[0]):
            #print("as1",as1)
            #print("as2",as2,"\n")
            count += 1
            
print(count)