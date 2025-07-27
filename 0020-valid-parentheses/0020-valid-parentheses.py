class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s :
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if char == brackets[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        if len(stack)== 0:
            return True
        else:
            return False
    
