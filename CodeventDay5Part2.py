import sys
import string

#iITJoOyRrYiIXxjgLlGrRnSsShHsNqQdNngGDwNHhDgGWwaAjSsJdnLlOogGAaPpkKEsaASeKkgGFfgGIQqZoOzPpiWHxXDdXCyYcDdxlygGYLTtdDQqsqQIiMnNmzZSsoOOzZGgoSbBg
if __name__ == '__main__':
    polymer = raw_input("Eyyy:")
    polymer2=polymer
    ans=""
    i=0
    y = 50000
    ans=""
    print len(polymer)
    alphabet = string.ascii_lowercase[:26]
    raw_input()
    for letter in alphabet:
        polymer = polymer2
        i=0
        while i < len(polymer)-1:
            if polymer[i] == letter or polymer[i] == letter.upper():
                # print polymer
                # print "Index:" + str(i) + ", " + polymer[i]
                polymer=polymer[0:i] + polymer[i+1:len(polymer)]
                # print polymer
                if i > 1:
                    i -= 2
                else:
                    i = -1
                # raw_input()
            i+=1
        i=0
        while i < len(polymer) - 1:
            if ((polymer[i].isupper() and polymer[i + 1].islower()) or (
                    polymer[i].islower() and polymer[i + 1].isupper())) and polymer[i].lower() == polymer[
                i + 1].lower():
                # print polymer
                # print "Index:" + str(i) + ", " + polymer[i] + ":" + polymer[i+1]
                polymer = polymer[0:i] + polymer[i + 2:len(polymer)]
                # print polymer
                if i > 1:
                    i -= 2
                else:
                    i = -1
                # raw_input()
            i += 1
        print letter
        print polymer
        print len(polymer)
        print "\n"
        if len(polymer)<y:
            ans=letter
            y=len(polymer)

    print ans
    print y
