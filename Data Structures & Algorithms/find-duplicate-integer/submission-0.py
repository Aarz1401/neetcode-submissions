class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break

        # both are in cycle
        start = 0 
        while(start != slow):
            start = nums[start]
            slow = nums[slow]

        return slow         