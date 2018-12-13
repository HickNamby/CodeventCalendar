import sys

#iITJoOyRrYiIXxjgLlGrRnSsShHsNqQdNngGDwNHhDgGWwaAjSsJdnLlOogGAaPpkKEsaASeKkgGFfgGIQqZoOzPpiWHxXDdXCyYcDdxlygGYLTtdDQqsqQIiMnNmzZSsoOOzZGgoSbBg
if __name__ == '__main__':
    polymer = raw_input("Eyyy:")
    ans=""
    i=0
    y = 500
    print len(polymer)
    raw_input()
    while i < len(polymer)-1:
        if ((polymer[i].isupper() and polymer[i+1].islower()) or (polymer[i].islower() and polymer[i+1].isupper())) and polymer[i].lower() == polymer[i+1].lower():
            # print polymer
            # print "Index:" + str(i) + ", " + polymer[i] + ":" + polymer[i+1]
            polymer=polymer[0:i] + polymer[i+2:len(polymer)]
            # print polymer
            if i > 1:
                i -= 2
            else:
                i = -1
            # raw_input()
        i+=1
    print polymer
    print len(polymer)
