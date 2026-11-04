import string 
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        # alphabet = set(string.ascii_letters + string.digits)
        strings=[]
        s=s.lower()
        
       
        strings = [char for char in s if char.isalnum()]

        return strings == strings[::-1]
            
        
        
        