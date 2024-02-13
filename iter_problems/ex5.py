def maximumUnits(boxTypes, truckSize):
    size = 0
    count = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    for box_type in boxTypes:
        if count >= truckSize:
            break
        else:
            box_total = min(box_type[0], truckSize - count)
            size += box_total * box_type[1]
            count += box_total
    
    return size



solution1 = maximumUnits([[1,3],[2,2],[3,1]], 4)
solution2 = maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)

print(solution1)
print(solution2)