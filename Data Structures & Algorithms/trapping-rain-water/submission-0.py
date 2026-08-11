class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_l = 0
        max_r = 0
        total_vol = 0
        while(l!=r):
            max_l = max(max_l,height[l])
            max_r = max(max_r,height[r])
            volume = 0
            if(height[l] < height[r]):
                volume = max(0,max_l - height[l])
                l += 1
            else :
                volume = max(0,max_r - height[r])
                r -= 1
            total_vol += volume
        return total_vol
            
            


                




            
        



             


        