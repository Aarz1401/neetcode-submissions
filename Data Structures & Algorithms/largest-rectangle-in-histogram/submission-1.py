class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        first_less_left = [-1] * len(heights) #indices of left boundary
        first_less_right = [len(heights)] * len(heights) #stores indices of right boundary

        stack = [] #store height, index pairs

        for i, height in enumerate(heights): 
            while stack and height < stack[-1][0]: #height is less than top
                h, index = stack.pop()
                first_less_right[index] = i
            stack.append((height, i))
        
        #now reverse for indices of left boundary
        heights_reversed = heights[::-1]
        stack = []

        for i, height in enumerate(heights_reversed): 
            while stack and height < stack[-1][0]: #height is less than top
                h, index = stack.pop()
                first_less_left[index] = len(heights) - 1 - i
            stack.append((height, i))
        
        first_less_left = first_less_left[::-1]

        max_area = -1
        for i,height in enumerate(heights):
            area = height * (first_less_right[i] - first_less_left[i] - 1)
            max_area = max(max_area,area)
        return max_area





        

