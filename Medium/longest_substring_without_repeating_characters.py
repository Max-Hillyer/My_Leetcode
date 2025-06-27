#Max Hillyer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        longest = ''

        for char in s:
            if char not in temp:
                temp += char
            else:
                if len(temp) > len(longest):
                    longest = temp
                # Remove up to and including the first duplicate character
                dup_index = temp.index(char)
                temp = temp[dup_index+1:] + char

        if len(temp) > len(longest):
            longest = temp

        return len(longest)
