class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum = prices[0]
        maximum = 0 
        
        for price in prices[1:]:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                if profit > maximum:
                    maximum = profit

        return maximum


