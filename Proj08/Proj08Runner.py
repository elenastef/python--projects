def run (aList, aChar):
    print("Elena Stefanova")
    print(aChar)
    print(aList)
    filteredList = []

    for word in aList:
        if aChar not in word:
            filteredList.append(word)

    return filteredList
