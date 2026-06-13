def romanToInt(s):
    res = 0
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    lenght = len(s)
    for idx, c in enumerate(s):
        current = nums[c]
        if idx+1 < lenght and current < nums[s[idx+1]]:
            res -= current
        else:
            res += current
    return res

