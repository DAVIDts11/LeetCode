class Solution:
    def romanToInt(self, s: str) -> int:
        RtoIDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        index = 0
        result = 0 

        if len(s)==1:
            result = RtoIDict[s[0]]
        else:
            while index<len(s)-1:
                if RtoIDict[s[index]]>=RtoIDict[s[index+1]]:
                    result+=RtoIDict[s[index]]
                    index+=1

                else:
                    result+=(RtoIDict[s[index+1]] - RtoIDict[s[index]])
                    index+=2
                
                if index==len(s)-1:
                    result+=RtoIDict[s[index]]

        return result

