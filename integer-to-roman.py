# Integer to Roman

def intToRoman(num: int) -> str:
    dic = { 1:      'I',
            5:      'V',
            10:     'X',
            50:     'L',
            100:    'C',
            500:    'D',
            1000:   'M'  
           }
    sub = { 'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M'] 
          }
    roman = ''
    decimal_place = 1
    while num:
        curr = num % 10 * decimal_place
        if curr in dic:

        decimal_place *= 10
        num = num // 10

# Driver code
cases = [3, 4, 9, 58, 1994, 99]

