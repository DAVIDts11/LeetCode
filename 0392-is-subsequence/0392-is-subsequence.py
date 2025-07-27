class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i<len(s):
            while j<len(t):
                if s[i]!=t[j]:
                    j+=1
                else:
                    j+=1
                    break
            
            if j == len(t):
                if i== len(s)-1 and s[i] == t[j-1]:
                    return True
                else:
                    return False            
            i+=1
        else:
            return True