class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        list_1 = list(s)
        list_2 = list(t)

        return sorted(list_1)==sorted(list_2)
            
            