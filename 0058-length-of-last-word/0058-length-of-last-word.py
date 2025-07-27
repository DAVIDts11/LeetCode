class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_started = False
        counter = 0 
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " : 
                if word_started:
                    break
                else:    
                    continue

            else:  
                word_started = True
                counter+=1

        return counter
        