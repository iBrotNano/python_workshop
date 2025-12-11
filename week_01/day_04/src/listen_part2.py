colorList = ["blue", "green", "yellow", "cyan", "pink", "violet", "orange"]
selection = colorList[:3]
promptText = ", ".join(selection)
print(promptText)

sortedList = colorList[:]
sortedList.sort()
print(sortedList)

sortedList.sort(reverse=True)
print(sortedList)
sortedList = sorted(sortedList, reverse=True)
print(sortedList)

print(colorList)
reversedList = colorList[:]
reversedList.reverse()
print(reversedList)

sortedReversedList = colorList[:]
sortedReversedList.sort()
sortedReversedList.reverse()
print(sortedReversedList)

numberList = list(range(1, 11))
print(numberList)
sameValuesList = numberList[::1]
print(sameValuesList)
revNumList = numberList[::-1]
print(revNumList)
revEvenNumList = numberList[::-2]
print(revEvenNumList)
revNumList = numberList[::-3]
print(revNumList)

revNumList = numberList[10:0:1]
print(revNumList)

revNumList = numberList[9:0:-1]
print(revNumList)

revNumList = numberList[9:0:-1]
print(revNumList)

revNumList = numberList[-1:-5:-1]
print(revNumList)

revNumList = numberList[-1::-1]
print(revNumList)

revNumList = numberList[-4::-1]
print(revNumList)

evens = numberList[1::2]
print(evens)

odds = numberList[::2]
print(evens)

revNumList = numberList[-8:-2:-2]
print(revNumList)

revNumList = numberList[-2:-8:-2]
print(revNumList)

revNumList = numberList[7:2:-3]
print(revNumList)

revNumList = numberList[-9:-3:2]
print(revNumList)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

checkNum = 4

if checkNum in numberList:
    print("4 is in list")
else:
    print("4 is not in list")

if "pink" in colorList:
    print("pink is in list")

numberList1 = numberList[:]
numberList2 = numberList[:]

del numberList1[:]
numberList2.clear()
print(numberList1)
print(numberList2)