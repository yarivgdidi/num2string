dict = [
    ['אפס', 'אחד', 'שניים', 'שלוש', 'ארבע', 'חמש', 'שש', 'שבע', 'שמונה', 'תשע'],
    ['עשרה', 'עשר', 'עשרים', 'שלושים','ארבעים', 'חמשים', 'שישים', 'שיבעים', 'שמונים', 'תשעים']
    ['מאות', 'מאה', 'מאתיים',  ]
]

def oneDigit(digit):
    return dict[0][digit]

def twoDigits(first, second):
    if(second == 0 ):
        return dict[1][first]
    elif (first == 1):
        return dict[0][second] + dict[1][0]
    else:
        return dict[1][first] + ' ו' + dict[0][second]

def threeDigits(first, second, last):
    if ()

def main():
    print(oneDigit(0))
    print(oneDigit(3))
    print(twoDigits(1,0))
    print(twoDigits(2, 0))
    print(twoDigits(1, 1))
    print(twoDigits(1, 9))
    print(twoDigits(2,1))
    print(twoDigits(2,2))
    print(twoDigits(3,3))
    print(twoDigits(9, 9))

main()