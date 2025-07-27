class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # index = haystack.find(needle)
        # return index
        i = 0
        while i<len(haystack):
            if haystack[i] == needle[0]:
                index = i
                if len(haystack)-i >= len(needle):
                    is_sum_string = True
                    for j in range(1,len(needle)):
                        i+=1
                        if haystack[i] != needle[j] :
                            is_sum_string =False
                            break
                    if is_sum_string:
                        return index
                    else:
                        i = index
                else:
                    return -1
                    
            i+=1        

        return -1