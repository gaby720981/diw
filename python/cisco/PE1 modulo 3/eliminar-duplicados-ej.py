myList = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]

resultantList = []
 
for element in myList:
    if element not in resultantList:
        resultantList.append(element)

print(resultantList)