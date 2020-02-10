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

def loadFile(fileName):
    contents=list()
    with open(fileName) as f:
        for line in f:
            contents.append(line)
    return contents

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
if memory_type == ('default'):
    print('to end conversation simply type goodbye ')
    endprogram = "goodbye"
    user = input('user:')
    while user != endprogram:
        lst = loadFile("memory.txt")
        tmpId = findBestId(user, lst) + 1
        if tmpId >= len(lst):
            tmpId = 0
        print(lst[tmpId])
        user = input('user: ')
    print("bye")
elif memory_type == ('Ordis'):
    print('to en conversation simply type goodbye as shown')
    endprogram = "goodbye"
    user = input('user:')
    while user != endprogram:
        lst = loadFile("Ordis.txt")
        tmpId = findBestId(user, lst) + 1
        if tmpId >= len(lst):
            tmpId = 0
        print(lst[tmpId])
        user = input('user:')
    print("bye")
else:
    print('no such memory exsist please type another or be sure you are typing it correctly as it appears.')




