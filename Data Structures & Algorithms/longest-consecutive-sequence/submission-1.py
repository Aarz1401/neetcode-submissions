class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        longest = 0
        for num in hashSet:
            if (num - 1) in hashSet:
                continue
            else:
                length = 1
                while(num + length) in hashSet:
                    length+=1
                if(length>longest):
                    longest = length
        return longest





        