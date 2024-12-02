from collections import Counter

with open("data.txt") as file:
    # Part 1
    finalDIff = 0
    leftArray = []
    rightArray = []
    for line in file:
        left, right = line.split("   ")
        leftArray.append(int(left))
        rightArray.append(int(right))
    leftSorted = sorted(leftArray)
    rightSorted = sorted(rightArray)
    for i in range(len(leftSorted)):
        l, r = leftSorted[i], rightSorted[i]
        larger = max(l, r)
        diff = 0
        if larger == r:
            diff = larger - l
        else:
            diff = larger - r
        finalDIff += diff
    print("Part 1 Solution: ", finalDIff)

    # Part 2
    rightCounter = Counter(rightSorted)
    similarity = 0
    for num in leftSorted:
        if rightCounter.get(num):
            similarity += num * rightCounter.get(num)
    print("Part 2 Solution: ", similarity)