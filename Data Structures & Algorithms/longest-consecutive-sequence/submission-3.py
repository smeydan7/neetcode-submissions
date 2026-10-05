class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        candidates = []
        for i in num_set:
            if i - 1 not in num_set:
                candidates.append(i)
        
        seqLen = 1
        maxSeq = 0
        for j in candidates:
            while seqLen < len(num_set):
                if (j + seqLen) in num_set:
                    seqLen += 1
                else:
                    break
            if seqLen > maxSeq:
                maxSeq = seqLen
            seqLen = 1
        return maxSeq