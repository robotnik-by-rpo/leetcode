def intToRoman( num):
    letters = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90: 'XC',
        100:'C',
        400:'CD',
        500:'D',
        900: 'CM',
        1000:'M',
        }
    
    res = ""
    for value, symbol in sorted(letters.items(),reverse=True):
        while num >= value:
            res += symbol
            num -= value
    return res

def intToRoman2( num: int) -> str:
    digits= {
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"    
    }
    res=""
    for i in digits.keys():
        res+=digits[i]*(num//i)
        print(digits[i]*(num//i))
        num=num%i
        
    return res

print(intToRoman2(3749))
