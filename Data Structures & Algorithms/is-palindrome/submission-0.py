class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings=[]
        s=s.lower()
        new_str = s.strip()
        for char in new_str:
            if char.isalnum():
                strings.append(char)

        return strings == strings[::-1]
            
        
        
        