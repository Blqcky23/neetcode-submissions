class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum = prices[0]
        maximum = 0 
        
        for i,num in enumerate(prices):
            if minimum>prices[i]:
                minimum = prices[i]
            
            else:
                profit = prices[i]- minimum
                if profit > maximum:
                    maximum = profit 

        return maximum 


