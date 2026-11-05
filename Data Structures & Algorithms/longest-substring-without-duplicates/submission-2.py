class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maximum = 0 
        left = 0 
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left+=1 



            seen.add(char)
            maximum = max(maximum,(right-left)+1)

        return maximum