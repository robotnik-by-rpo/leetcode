def longestCommonPrefix( strs: list[str]) -> str:
    res = ""
    for combo in zip(*strs):
        if len(set(combo)) == 1:
            res += combo[0]
        else:
            break
    return res