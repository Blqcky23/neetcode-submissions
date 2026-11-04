import string 
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        alphabet = set(string.ascii_letters + string.digits)
        strings=[]
        s=s.lower()
        
        for char in s:

            # if char.isalnum():
            if char in alphabet:
                strings.append(char)

        return strings == strings[::-1]
            
        
        
        