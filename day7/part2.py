class Directory:
	def __init__(self,dirName):
		self.dirName = dirName
		self.directories = []
		self.filesize = 0
	def addDirectories(self,add):
		self.directories.append(add)
	def addFiles(self,size):
		self.filesize += size	
	def geName(self):
		return self.dirName
		
	def __str__(self):
		return '.'.join(self.dirName)

current_dir = []
directories = []
with open("puzzle.txt","r",encoding="utf-8") as file:
	new = None
	for line in file:
		if "$ cd" in line:
			line = line.strip()
			line = line.split(" ")
			if line[2] == "..":
				current_dir.pop()
			else:
				current_dir = current_dir + [line[2]]
		elif "$ ls" in line:
			line = line.strip()
			line = line.split(" ")
			new = Directory(current_dir.copy())
			if str(new) not in directories:
				directories.append(new)
		elif "dir" in line:
			line = line.strip()
			line = line.split(" ")
			new.addDirectories(current_dir.copy() +[line[1]])
		else:
			line = line.strip()
			line = line.split(" ")
			new.addFiles(int(line[0]))

valuesOfDirectories = {}

for i in directories:
	if len(i.directories) == 0:
		directories.remove(i)
		valuesOfDirectories[str(i)] = i.filesize 

while len(directories) > 0:
	for i in directories:
		length = len(directories)
		fillIn = True
		for y in i.directories:
			if ".".join(y) not in valuesOfDirectories:
				fillIn = False
		if fillIn == True:
			total = i.filesize
			for y in i.directories:
				total += valuesOfDirectories[".".join(y)]
			valuesOfDirectories[str(i)] = total
			directories.remove(i)
	if len(directories) == length:
		break

# sams part two attempt
freespace = 70000000 - valuesOfDirectories["/"]
spaceNeeded = 30000000 - freespace
lowest = 70000000
for i in valuesOfDirectories.values():
	if i >= spaceNeeded and i<=lowest:
		lowest = i

print(lowest)