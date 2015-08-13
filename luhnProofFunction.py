#!/usr/env/python3

# no module dependancies 
# Python 3 Implementation of the Luhn Algorithm
# Checks to see if 14, 15 or 16 digit account number is Luhn Compliant.  
# See https://en.wikipedia.org/wiki/Luhn_algorithm for formula details.  
# where cardNumber is an account number received as a string:

def doLuhn(cardNumber):
    cardLength = len(cardNumber)
    everyOtherFromFarRightFor16 = [-2,-4,-6,-8,-10,-12,-14,-16]
    everyOtherFromFarRightFor15 = [-2,-4,-6,-8,-10,-12,-14]
    everyOddFromFarRightButOneFor15 = [-3,-5,-7,-9,-11,-13,-15]
    everyOddFromFarRightButOneFor14 = [-3,-5,-7,-9,-11,-13]
    doubleList = []
    doubleSet = []
    addUpDoubles = 0
    addUpOthers = 0
    if (cardLength == 16):
        doubleList = everyOtherFromFarRightFor16
        addUpTheOddDigits = everyOddFromFarRightButOneFor15
    elif (cardLength == 15):
        doubleList = everyOtherFromFarRightFor15
        addUpTheOddDigits = everyOddFromFarRightButOneFor15
    elif (cardLength == 14):
        doubleList = everyOtherFromFarRightFor15
        addUpTheOddDigits = everyOddFromFarRightButOneFor14
    else:
        return(False)
    for each in doubleList:
        doubleThis = cardNumber[each]
        doubleThis = int(doubleThis) * 2
        nowDoubled = str(doubleThis)
        if (len(nowDoubled) == 1):
            nowDoubled = nowDoubled
            doubleSet.append(nowDoubled)
        else:
            db1, db2 = nowDoubled[0], nowDoubled[1]
            db1, db2 = int(db1), int(db2)
            dbladd = db1 + db2
            doubleSet.append(dbladd)
    for each in doubleSet:
        addUpDoubles += int(each)
    print('addUpDoubles:', addUpDoubles)
    for each in addUpTheOddDigits:
        addOther = cardNumber[each]
        otherToAdd = int(addOther)
        addUpOthers += otherToAdd
    print('addUpOthers:', addUpOthers)
    totalSum = int(addUpDoubles) + int(addUpOthers)
    print('totalSum:', totalSum)
    totalSumTimesNine = (totalSum * 9)
    modTheTotalSum = (totalSumTimesNine % 10)
    if (str(modTheTotalSum) == cardNumber[-1]):
        return(True)
    else:
        return(False)

