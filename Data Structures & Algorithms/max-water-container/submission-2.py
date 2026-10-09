class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = (r - l) * min(heights[l], heights[r])
        while l < r:
            currH = (r - l) * min(heights[l], heights[r])
            if currH > maxHeight:
                maxHeight = currH
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxHeight
        