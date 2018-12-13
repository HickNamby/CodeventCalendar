import sys

if __name__ == '__main__':
    instring = sys.stdin.readlines()
    total =0
    freqDic = {"0": 1}
    firstDupe =True
    dupeFreq=0
    while firstDupe:
        for num in instring:
            total+=int(num)
            if (freqDic.get(total)==None):
                freqDic[total]=0
            freqDic[total]+=1
            if (freqDic[total]==2):
                dupeFreq=total
                firstDupe=False
                break

    print ("Final: " + str(total) + "\n")
    print ("First Dupe: " + str(dupeFreq))

