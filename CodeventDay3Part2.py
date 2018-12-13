import sys

if __name__ == '__main__':
    strlist = sys.stdin.readlines()

    fabric = [[0 for i in range(999)] for j in range(999)]
    ansArea=0

    patterns=[]
    for string in strlist:
        # Split string by spaces
        split1 = string.split()

        # Get ID
        id=split1[0].strip("#")

        #Get coords of start
        startCoord=split1[2].strip(":")
        xStart=int(startCoord.split(",")[0])
        yStart=int(startCoord.split(",")[1])

        #Get length and width of pattern
        dimensions=split1[3]
        width=int(dimensions.split("x")[0])
        height=int(dimensions.split("x")[1])

        #               [0]             [1]                 [2]               [3]                 [4]
        patterns.append(id + " " + str(xStart) + " " + str(yStart) + " " + str(width) + " " + str(height))

        for w in range(width):
            for h in range(height):
                fabric[xStart+w][yStart+h]+=1

         #END STRING HANDLE LOOP

    ansXStart=0
    ansYStart=0
    ansWidth=0
    ansHeight=0
    for pattern in patterns:
        keepLookin = True
        splitPattern=pattern.split()
        for i in range(int(splitPattern[3])):
            if keepLookin:
                for j in range(int(splitPattern[4])):
                    if fabric[i+int(splitPattern[1])][j+int(splitPattern[2])]!=1:
                        keepLookin=False
                        break
            else:
                break
        if keepLookin:
            print pattern