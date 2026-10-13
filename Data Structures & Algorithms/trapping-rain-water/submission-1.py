class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l_max = [0] * len(height) 
        l_max_value = height[0]
        r_max = [0] * len(height) 
        r_max_value = height[len(height) - 1]
        i = 0
        for left in height:
            if left > l_max_value:
                l_max_value = left
            l_max[i] = l_max_value
            i += 1
        i = len(height) - 1
        for right in height[::-1]:
            if right > r_max_value:
                r_max_value = right
            r_max[i] = r_max_value
            i -= 1
        
        total_water = 0
        for j in range(len(height)):
            add = min(l_max[j], r_max[j]) - height[j]
            if add < 0:
                add = 0
            total_water += add

        return total_water
