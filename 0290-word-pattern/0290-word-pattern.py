class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        matches = {}
        s_words = s.split()
        if len(pattern)!= len(s_words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in matches: 
                if s_words[i] in matches.values():
                    return False
                else:
                    matches[pattern[i]] = s_words[i]
            else:
                if  matches[pattern[i]] != s_words[i]:
                    return False
        return True