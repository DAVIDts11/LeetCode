class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefex = strs[0]
        for curr_string in strs[1:]:
            length = min(len(prefex),len(curr_string))
            prefex = prefex[:length]
            for i in range(length):
                if prefex[i] != curr_string[i]:
                    prefex = prefex[:i]
                    break       
            if len(prefex) == 0:
                break
        
        return  prefex
