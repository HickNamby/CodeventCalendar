import sys
class SleepyCop:
    def __init__(self, id):
        self.id = id
        self.total=0
        self.sleepMinutes=[0 for i in range(60)]
        self.daysOnJob=0

    def getId(self):
        return self.id

    def addToTotal(self, num):
        self.total=num+self.total

    def getTotal(self):
        return self.total

    def addToSleepMinutes(self, minute):
        self.sleepMinutes[minute]+=1

    def getSleepMinutes(self):
        return self.sleepMinutes

    def setDaysOnJob(self, num):
        self.daysOnJob=num

    def getDaysOnJob(self):
        return self.daysOnJob

    def __repr__(self):
        return str(self.__dict__)

if __name__ == '__main__':
    strlist = sys.stdin.readlines()
    strlist.sort()

    activeGuard=""
    guardSleepNumbers={}
    startSleep = 0
    stopSleep = 0
    for string in strlist:
        spstring=string.strip("\n").split()
        print spstring

        date = spstring[0].strip("[")
        time = spstring[1].strip("]")
        minute=time.split(":")[1]


        if spstring[2]=="Guard":
            activeGuard=spstring[3].strip("#")
            if guardSleepNumbers.get(activeGuard) is None:
               guardSleepNumbers[activeGuard] = SleepyCop(activeGuard)
            else:
               guardSleepNumbers[activeGuard].setDaysOnJob(guardSleepNumbers[activeGuard].getDaysOnJob()+1)

        if spstring[2]=="falls":
            startSleep=int(minute)
        if spstring[2]=="wakes":
            stopSleep=int(minute)
            print "Start @" + str(startSleep) + ", End @" + str(stopSleep) + ", Total = " + str(stopSleep-startSleep)
            guardSleepNumbers[activeGuard].addToTotal(stopSleep-startSleep)
            for i in range(startSleep, stopSleep):
                guardSleepNumbers[activeGuard].addToSleepMinutes(i)

        # print "Date: " + date + " -- Time: " + time + " -- Guard: " + activeGuard +"\n"

    # print guardSleepNumbers
    highScore=0
    highId=""
    for key in guardSleepNumbers:
        guard=guardSleepNumbers[key]
        if guard.getTotal()>highScore:
            highScore=guard.getTotal()
            highId=guard.getId()
    print guardSleepNumbers[highId]
    print guardSleepNumbers[highId].getSleepMinutes().index(max(guardSleepNumbers[highId].getSleepMinutes()))

    # print "High ID: "+ str(highId) + " -- High Score: " + str(highScore)