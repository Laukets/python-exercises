def applyRules(ch):
    newstr = ""
    if ch == 'A':
        newstr = 'B' # rule 1
    elif ch == 'B':
        newstr = 'AB' # rule 2
    else:
        newstr = ch # no rules apply so keep the character
    return newstr

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

print(createLSystem(4, 'A'))