class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = 0
        for i in nums:
            if i == 0:
                result += 1
            else:
                product *= i
        
        if result >= 2:
            return [0 for num in nums]
        elif result == 1:
            return [product if num == 0 else 0 for num in nums]
        else:
            return [product // num for num in nums
            ]