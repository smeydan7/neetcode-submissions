class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrams = {}
        print(angrams)
        for s in strs:
            currSorted = "".join(sorted(s))
            if currSorted not in angrams:
                angrams[currSorted] = []

            angrams[currSorted].append(s)
        return list(angrams.values())
        