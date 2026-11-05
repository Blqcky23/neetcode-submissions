class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        width = (right - left)
        
        maximum = (len(heights)-1) * min(heights[0],heights[-1])
        print(maximum)
        while(left<right):
            
            if heights[left]>=heights[right]:   
                right-=1
                
            elif heights[left]<heights[right]: 
                left+=1

            new_max = (right-left )* min(heights[left],heights[right])
            
            print(new_max)
            if new_max>maximum:
                maximum = new_max

        return maximum