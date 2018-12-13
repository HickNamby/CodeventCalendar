import sys

if __name__ == '__main__':
    strlist = sys.stdin.readlines()
    i=0
    ans1=""
    ans2=""
    stop=False
    for string in strlist:
        if stop:
            break
        j = i + 1
        string=string.strip()
        # print ("Primary String: " + string)
        while j<len(strlist):
            string2 = strlist[j].strip()
            # print ("\t" + string2)
            diffCount=0
            l=0
            for letter in string:
                # print "Letter=" + letter + ", L=" + str(l)
                if letter != string2[l]:
                    diffCount+=1
                l += 1
            if diffCount==1:
                stop=True
                ans1=string
                ans2=string2
                print (ans1 + " : " + ans2)
            # print diffCount
            j+=1
        i+=1
    common=""
    i=0
    for letter in ans1:
        if letter==ans2[i]:
            common+=letter
        i+=1
    print common
