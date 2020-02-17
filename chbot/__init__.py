import files # File manager

#Distance
def __minimumEditDistance(s1,s2):
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

#finds the best sentence in a memory file to say.
def __findBestId(s1,lst):
    rid=0
    score=100000
    for i in range(len(lst)):
        tmpScore=__minimumEditDistance(s1,lst[i])
        if tmpScore<score:
            score=tmpScore
            rid=i
    return rid

def chatbot(file):
    endprogram = "goodbye"
    print('to end conversation simply type '+endprogram+'.')
    user = input('user:')
    while user != endprogram:
        #this is where the distance is used to compare the users input to the chosen txt file, finds the best similarity and prints it as a response
        lst = files.loadFile(file)
        tmpId = __findBestId(user, lst) + 1
        if tmpId >= len(lst):
            tmpId = 0
        print(lst[tmpId])
        files.record(user+'\n') # The \n makes a new line
        user = input('user: ')
    print("bye")
