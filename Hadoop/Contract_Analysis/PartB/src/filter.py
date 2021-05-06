with open("ContractAnalysisPartB.txt") as f:
    lines = f.readlines()


content = [x.strip() for x in lines]
recordList = []


for line in content:
    info = line.split("\t")
    recordList.append((info[0],int(info[1])))

def findMax():
    max = recordList[0][1]
    index = 0
    for i in range(len(recordList)):
        if max<recordList[i][1]:
            max = recordList[i][1]
            index = i
    return index


for i in range(20):
    j = findMax()
    print ("%s\t%d" % (recordList[j][0],recordList[j][1]))
    recordList.pop(j)