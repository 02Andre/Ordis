#Distance
def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]
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

#finds the best sentence in a memory file to say.
def findBestId(s1,lst):
    rid=0
    score=100000
    for i in range(len(lst)):
        tmpScore=minimumEditDistance(s1,lst[i])
        if tmpScore<score:
            score=tmpScore
            rid=i
    return rid
#gives user the option to use a different memory.txt file
print('before you can start talking please type what memory you want the bot to have.')
print('options: default or Ordis')
memory_type = input('type:')
#the user will be in a while loop until they type the correct memory option
while memory_type != 'default' and memory_type != 'Ordis':
    print('no such memory exsits please choose from the options or check if its spelled right.')
    memory_type = input('type: ')
#if user want the default memory this will activate
if memory_type == ('default'):
    print('to end conversation simply type goodbye ')
    endprogram = "goodbye"
    user = input('user:')
    while user != endprogram:
        #this is where the distance is used to compare the users input to the chosen txt file, finds the best similarity and prints it as a response
        lst = loadFile("memory.txt")
        tmpId = findBestId(user, lst) + 1
        if tmpId >= len(lst):
            tmpId = 0
        print(lst[tmpId])
        record(user)
        user = input('user: ')
    print("bye")
#this is the other memory option
elif memory_type == ('Ordis'):
    print('to end conversation simply type goodbye as shown')
    endprogram = "goodbye"
    user = input('user:')
    while user != endprogram:
        lst = loadFile("Ordis.txt")
        tmpId = findBestId(user, lst) + 1
        if tmpId >= len(lst):
            tmpId = 0
        print(lst[tmpId])
        record(user)
        user = input('user:')
    print("bye")
