class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        width = (right - left)
        maximum = 0 
    
        while(left<right):

            new_max = (right-left )* min(heights[left],heights[right])
            maximum =max(new_max,maximum)

            if new_max>maximum:
                maximum = new_max
            
            if heights[left]>=heights[right]:   
                right-=1
                
            elif heights[left]<heights[right]: 
                left+=1     

        return maximum