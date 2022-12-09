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
# abc->def
# ghd -> def
with open('puzzle.txt') as file:
	new = None
	for line in file:
		#print(line)
		if "$ cd" in line:
			line = line.strip()
			line = line.split(" ")
			#print("went here")
			if line[2] == "..":
				current_dir.pop()
			else:
				current_dir = current_dir + [line[2]]
				#print("line 2",line[2])
				#print("new",current_dir)
				#print(line[2])
		elif "$ ls" in line:
			line = line.strip()
			line = line.split(" ")
			new = Directory(current_dir.copy())
			if str(new) not in directories:
				directories.append(new)
		elif "dir" in line:
			line = line.strip()
			line = line.split(" ")
			# print("here is here",current_dir +[line[1]])
			new.addDirectories(current_dir.copy() +[line[1]])
		else:
			line = line.strip()
			line = line.split(" ")
			new.addFiles(int(line[0]))
#print("origional length",len(directories))
#print("\n\n\n\n\n\n")


# for i in directories:
# 	print(i,i.filesize)
valuesOfDirectories = {}

# print(''.join(["hello"," world"]))
# print( "this", directories[1].directories)
# print(len(directories))
for i in directories:
	if len(i.directories) == 0:
		directories.remove(i)
		valuesOfDirectories[str(i)] = i.filesize 
#print(len(directories))
#print("the values of directories",valuesOfDirectories)
while len(directories) > 0:
	for i in directories:
		length = len(directories)
		fillIn = True
		for y in i.directories:
			#print("here i am",y)
			#print("this is string object",str(i))
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
#print(len(directories))
#for i in directories:
#	print(i,"\n",i.directories)
maxTotal = 0
for i in valuesOfDirectories:
	if valuesOfDirectories[i] <= 100000:
		#print(i,"/n",valuesOfDirectories[i])
		maxTotal += valuesOfDirectories[i]