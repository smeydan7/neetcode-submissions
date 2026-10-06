class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 3:
            return [1, 2]

        index1 = 0
        index2 = length - 1

        i = 0
        while index1 != index2:
            currSum = numbers[index1] + numbers[index2]
            if currSum == target:
                return [index1 + 1, index2 + 1]
            if currSum < target:
                index1 += 1
            else: 
                index2 -= 1

        return [index1 + 1, index2 + 1]
