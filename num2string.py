dict = [
    ['אפס', 'אחת', 'שתיים', 'שלוש', 'ארבע', 'חמש', 'שש', 'שבע', 'שמונה', 'תשע'],
    ['עשרה', 'עשר', 'עשרים', 'שלושים','ארבעים', 'חמשים', 'שישים', 'שיבעים', 'שמונים', 'תשעים'],
    ['מאות', 'מאה', 'מאתיים' ],
    ['אלפים', 'אלף', 'אלפיים']
]

def oneDigit(digit):
    return dict[0][digit]

def twoDigits(first, second):
    if(second == 0 ):
        return dict[1][first]
    elif (first == 1):
        return dict[0][second] + ' ' + dict[1][0]
    else:
        return dict[1][first] + ' ו' + dict[0][second]

def threeDigits(first, second, last):
    if (not first and not second):
        return oneDigit(last)
    if (not first ):
        return twoDigits(second, last)

    result = ''
    if (first == 1 or first ==2):
        result += dict[2][first]
    else:
        result = dict[0][first] + ' ' + dict[2][0]

    if (second == 0 and last == 0):
        return result
    elif (second == 0):
        return result + ' ו' + oneDigit(last)
    elif (second == 1):
        return result + ' ו' + twoDigits(second, last)
    else:
        return result + ' ' + twoDigits(second, last)

def thousands(first, second, last):
    if (not first and not second):
       if last in [1, 2]:
           return dict[3][last]
       else:
           return dict[0][last].replace('ה', '') + 'ת ' + dict[3][0]
    elif (not first):
        if (second == 1 and last ==0):
            return 'עשרת אלפים'
        return twoDigits(second, last) + ' ' + dict[3][1]
    else:
        return threeDigits(first, second, last) + ' ' + dict[3][1]

def main():
    inputNum = ''
    while (True):
        inputNum = input("Choose a number, up to 6 digits, x to quit:")
        if (inputNum == 'x'):
            return
        number = []
        for i in (range(6-len(inputNum))):
            number.append(0)
        for i in range(len(inputNum)):
            number.append(int(inputNum[i]))

        if (len(inputNum) < 4 ):
            print(threeDigits(*number[3:]))
        else:
            separator = ' '
            if (inputNum[3:] == '000'):
                print(thousands(*number[0:3]))
            else:
                if (number[2] == 0):
                    separator = ' ו'
                print(thousands(*number[0:3]) + separator + threeDigits(*number[3:]))

main()