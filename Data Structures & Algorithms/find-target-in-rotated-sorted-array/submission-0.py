class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while(l<r):
            mid = (l+r) // 2
            if(nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid
        #l is now pointing to minimum element
        min_idx = l 
        r = len(nums) - 1

        #r at end
        #l is in center, r is at end
        if(nums[r] < target): #its in first half
            r = l  
            l = 0
            while(l<=r):
                mid = (l+r) // 2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] > target):
                    r = mid - 1
                else:
                    l = mid + 1
        else: #its in  second half
            l = min_idx
            r = len(nums) - 1
            while(l<=r):
                mid = (l+r) // 2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] > target):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
            

        


