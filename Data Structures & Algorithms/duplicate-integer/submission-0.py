class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for key in nums:
            if(key not in myDict):
                myDict[key]=0
            else:
                return True
        
        return False