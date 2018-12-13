import sys

if __name__ == '__main__':
    strlist = sys.stdin.readlines()

    twoLetterMatches = 0
    threeLetterMatches = 0

    for string in strlist:
        letterDic = {}
        twoMatch=False
        threeMatch=False
        for letter in string:
            if letterDic.get(letter)==None:
                letterDic[letter]=1
            else:
                letterDic[letter]+=1
        for entry in letterDic:
            if letterDic[entry]==2:
                twoMatch=True
            if letterDic[entry]==3:
                threeMatch=True
        if twoMatch:
            twoLetterMatches+=1
        if threeMatch:
            threeLetterMatches+=1

    checksum= twoLetterMatches*threeLetterMatches
    print checksum






