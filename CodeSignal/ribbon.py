import math

def maxLength(a, k):
    amountOfLength = {}
    for fullRibbonLength in a:
        prevSnippetLength = fullRibbonLength+1
        prevNumHarvested = 1
        for numHarvested in range(1, k+1):
            snippetLength = fullRibbonLength // numHarvested

            if snippetLength < 1:
                break

            for i in range(prevSnippetLength-1, snippetLength, -1):
                amountOfLength[str(i)] = amountOfLength.get(str(i), 0) + prevNumHarvested

            actualNumHarvested = fullRibbonLength // snippetLength
            amountOfLength[str(snippetLength)] = amountOfLength.get(str(snippetLength), 0) + actualNumHarvested

            prevSnippetLength = snippetLength
            prevNumHarvested = actualNumHarvested

    listOfKeys = sorted([int(key) for key in amountOfLength.keys()])
    listOfKeys.reverse()

    for key in listOfKeys:
        if amountOfLength[str(key)] >= k:
            return key



if __name__ == '__main__':
    a = [5, 2, 7, 4, 9]
    k = 5
    print(maxLength(a, k))
