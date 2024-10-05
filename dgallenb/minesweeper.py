def annotate(minefield):
    # Function body starts here
    # input is a 2d array of spaces and asterisks. Asterisk means bomb.

    if(checkValidity(minefield)):
        output = []
        if(len(minefield) < 1):
            return output
        for i in range(len(minefield)):
            #if(isinstance(minefield[i], str)):
            output += [""]
            for j in range(len(minefield[i])):
                if(minefield[i][j] == "*"):
                    output[i] += "*"
                else:
                    output[i] += countAdjacent(minefield, i, j)
        return output
                    
            
    else:
        raise ValueError("The board is invalid with current input.")
        

def checkValidity(minefield):
    if(isinstance(minefield, list)):
        if(len(minefield) < 1):
            return True
        for i in range(len(minefield)):
            if(isinstance(minefield[i], str)):
                if(len(minefield[i]) != len(minefield[0])):
                    return False;
                for j in range(len(minefield[i])):
                    if(not(minefield[i][j]==" ") and not(minefield[i][j]=="*")):
                        return False                   
            else:
                if(minefield[i] is None):
                    return True;
                else:
                    return False;
        return True;
    else:
        return false

def countAdjacent(minefield, row, col):
    minRow = max(0, row - 1)
    maxRow = min(len(minefield), row + 2)
    minCol = max(0, col - 1)
    maxCol = min(len(minefield[row]), col + 2)
    #print("row: " + str(minRow) + "-" + str(maxRow) + ", col: " + str(minCol) + "-" + str(maxCol))
    count = 0

    for i in range(minRow, maxRow):
        for j in range(minCol, maxCol):
            #print("[" + str(i) + "][" + str(j) + "]: " + minefield[i][j] + ", count: " + str(count) + ", isGood? " + str(minefield[i][j] == "*"))
            if(minefield[i][j] == "*"):
                
                count += 1;
                #print("found mine! Count is: " + str(count))
    if(count == 0):
        return " "
    return str(count);


def countSpot(minefield, row, col):
    return minefield[row][col] == "*"
