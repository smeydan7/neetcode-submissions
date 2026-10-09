class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = []
        if len(nums) <= 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [[nums[0], nums[1], nums[2]]]
        nums.sort()
        last_idx = {val: idx for idx, val in enumerate(nums)}
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            while j < (len(nums) - 1):
                currSum = nums[i] + nums[j]
                if 0 - currSum in last_idx and last_idx[0 - currSum] > j:
                    indices.append([nums[i], nums[j], 0 - currSum])
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
        
        return indices
