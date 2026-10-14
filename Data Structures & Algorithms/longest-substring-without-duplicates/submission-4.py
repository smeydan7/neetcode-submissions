class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if len(s) < 2:
            return 1

        seen = set()
        count = 0
        maxCount = 0
        
        l = 0
        r = l + 1
        maxDiff = r - l
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                if s[l] != s[r]:
                    while s[l] != s[r]:
                        l += 1
                while s[l] == s[r] and l < r:
                    l += 1
            if (r - l) > maxDiff:
                maxDiff = r - l

        return maxDiff
        
        