class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matches = {}
        for i in range(len(s)):
            if s[i] not in matches: 
                if t[i]  in matches.values():
                    return False
                else:
                    matches[s[i]] = t[i]
            else:
                if  matches[s[i]] != t[i]:
                    return False
        return True