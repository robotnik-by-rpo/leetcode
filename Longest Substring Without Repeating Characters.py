def lengthOfLongestSubstring( s: str) -> int:
    last = {}
    left = 0
    len_str = 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = right
        len_str = max(len_str, right - left + 1)
    return len_str

print(lengthOfLongestSubstring(s="abcabcbb"))
print(lengthOfLongestSubstring(s="bbbbb"))
print(lengthOfLongestSubstring(s="pwwkew"))
print(lengthOfLongestSubstring(s="ohomm"))
    