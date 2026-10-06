class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            length = len(s)
            string += str(length) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        seenNum = False
        num = 0
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        strings = []
        i = 0
        print(s)
        while i < len(s):
            if s[i].isdigit() and seenNum is False:
                seenNum = True
                if (i + 1) < len(s) and s[i + 1] == '#':
                    strLen = s[i]
                elif (i + 2) < len(s) and s[i + 2].isdigit():
                    strLen = s[i:i+3]
                elif (i + 1) < len(s) and s[i + 1].isdigit():
                    strLen = s[i:i+2]
            if seenNum is True and (s[i] == '#'):
                strings.append(s[i + 1:i + int(strLen) + 1])
                seenNum = False
                i += int(strLen)
            i += 1
        return strings

