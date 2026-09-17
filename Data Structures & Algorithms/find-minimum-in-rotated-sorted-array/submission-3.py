class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find where rotation is
        # rotated array has a point where max meets min
        l = 0
        r = len(nums) - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] > nums[r]): #same segment for mid and r
                l = mid + 1
            else:
                r = mid 
        return nums[l]

        