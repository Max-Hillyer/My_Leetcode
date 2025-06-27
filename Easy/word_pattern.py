#max Hillyer 6/26/25

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patword = {}
        words = s.split()
        if len(list(pattern)) != len(words):
            return False
        for i,key in enumerate(pattern):
            if key not in patword.keys() and words[i] not in patword.values():
                patword[key] = words[i]
        for i,j in zip(words,pattern):
            if patword.get(j) != i:
                return False
        return True
