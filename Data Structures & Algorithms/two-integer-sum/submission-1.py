class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 3:
            return [0, 1]
        hashmap = {}
        index = 0;
        for i in nums:
            if (target - i) in hashmap:
                return [hashmap[target - i], index]
            hashmap[i] = index
            index += 1
        
            