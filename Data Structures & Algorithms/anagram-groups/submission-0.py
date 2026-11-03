class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dics ={}
        for string in strs: 
            sorted_string = "".join(sorted(string))
            if sorted_string in dics:
                dics[sorted_string]=dics[sorted_string]+[string]
            else:
                dics[sorted_string]=[string]

        wynik = list(dics.values())
        
        return wynik