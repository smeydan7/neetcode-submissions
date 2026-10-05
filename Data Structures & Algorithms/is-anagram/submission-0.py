class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted_text = "".join(sorted(s))
        t_sorted = sorted_text = "".join(sorted(t))

        return s_sorted == t_sorted