#loads the chosen memory file
def loadFile(fileName):
    contents=list()
    with open(fileName) as f:
        for line in f:
            contents.append(line)
    return contents
#lets program write the user response in the memory file
def record(user):
    file=open('log.txt', 'a')
    file.write(user)
    file.close()
