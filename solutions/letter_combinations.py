def letterCombinations(digits: str):
    dic = { '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
    digits_len = len(digits)
    words_len = 1
    arr = [1 for _ in range(digits_len)]
    for i, c in reversed(list(enumerate(digits))):
        words_len *= len(dic[c])
        arr[i] = 1 if i==digits_len-1 else len(dic[digits[i+1]])*arr[i+1]
    words = ['' for _ in range(words_len)]
    print(words, arr)
    for i, c in enumerate(digits):
        for j in range(len(dic[c])):
            for k in range(arr[i]):
                for l in range(words_len//len(dic[c])):
                    print((j*arr[i]+k))
                    #print(j*arr[i]+k, dic[c][j],words[(j*arr[i])+k])
                    #words[(j*arr[i])+k]+=dic[c][j]
    print(words)

letterCombinations('27')