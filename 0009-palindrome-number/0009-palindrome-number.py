class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i,j = 0,(len(s)-1)
        while s[i]==s[j]:
            if i==j or j==i+1:
                return True
            else:
                i+=1
                j-=1
        else:
            return False
