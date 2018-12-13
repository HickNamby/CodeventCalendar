import sys

if __name__ == '__main__':
    strlist = sys.stdin.readlines()

    fabric = [[0 for i in range(999)] for j in range(999)]
    ansArea=0

    for string in strlist:
        # Split string by spaces
        split1 = string.split()

        # Get ID
        id=split1[0]

        #Get
        startCoord=split1[2].strip(":")
        xStart=int(startCoord.split(",")[0])
        yStart=int(startCoord.split(",")[1])

        dimensions=split1[3]
        width=int(dimensions.split("x")[0])
        height=int(dimensions.split("x")[1])

        for w in range(width):
            for h in range(height):
                fabric[xStart+w][yStart+h]+=1

         #END STRING HANDLE LOOP
    for i in range(999):
        for j in range(999):
            if fabric[i][j]>=2:
                ansArea+=1
    print ansArea



        # print "id:" + id + " -- xStart:" + xStart + " -- yStart:" + yStart + " -- width:" + width + " -- height:" + height