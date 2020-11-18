def getRow(rowIndex):
    curr = [1]
        
    for i in range(rowIndex):
        nextRow = [1]
            
        for j in range(1, len(curr)):
            nextRow.append(curr[j] + curr[j - 1])
                
        nextRow.append(1)
        curr = nextRow
            
    return curr