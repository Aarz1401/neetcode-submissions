class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        count = 0
        for i in nums:
            if ((target - i) in seen):
                return [seen[target - i],count]
            else:
                seen[i] = count
            count += 1
        return[]

        