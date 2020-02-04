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


#file read
def searchfile():
    f=open("memory.txt", "r")
    if f.mode == 'r':
        contents =f

def loadFile(fileName):
    contents={}
    f = open(fileName, "r")
    if f.mode == 'r':
        contents = f
    return contents

def findBestId(s1,lst):
    rid=0
    score=100000
    for i in range(lst.length()):
        tmpScore=minimumEditDistance(s1,lst[i])
        if tmpScore<score:
            score=tmpScore
            rid=i
    return rid

#user input
user = input('')
lst=loadFile("memory.txt")
tmpId=findBestId(user,lst)+1
if tmpId>=lst.length():
    tmpId=0
print(lst[tmpId])