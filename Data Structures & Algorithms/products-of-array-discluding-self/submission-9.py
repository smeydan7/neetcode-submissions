class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = nums.count(0)
        if result > 1:
            product = 0
        for i in nums:
            if i == 0:
                continue
            product *= i
        products = []
        for j in range(len(nums)):
            if nums[j] == 0:
                products.append(product)
            else:
                if result > 0:
                    products.append(0)
                else:
                    products.append(product // nums[j])
        return products