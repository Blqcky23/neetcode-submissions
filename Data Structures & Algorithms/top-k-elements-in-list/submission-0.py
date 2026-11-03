class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1

        top_keys = sorted(seen, key=seen.get,reverse=True)[:k]

        return top_keys