class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict = {}
        for i,num in enumerate(numbers):
            if(target-num in myDict):
                return [myDict[target-num],i+1]
            else:
                myDict[num]=i+1
        return []

        