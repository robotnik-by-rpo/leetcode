from typing import List


def maxArea(height: List[int]) -> int:
    
    max_val = 0
    lenght = len(height)
    right = lenght-1
    left = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        temp = width*h 
        max_val = max(max_val, temp)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_val

print(maxArea(height=[1,8,6,2,5,4,8,3,7]))
print(maxArea(height=[1,1]))