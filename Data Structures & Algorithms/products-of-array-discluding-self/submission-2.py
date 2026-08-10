class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        output = [1] * len(nums)
        zeroinNums = False
        indexZero = []
        count = 0
        for num in nums:
            if(num == 0):
                zeroinNums = True
                totalProduct *= 1
                indexZero.append(count)
            else :
                totalProduct *= num
            count += 1


        for i in range(len(nums)):
            if zeroinNums:
                if i in indexZero and (len(indexZero) == 1):
                    output[i] = totalProduct
                else:
                    output[i] = 0
            else:
                output[i] = int(totalProduct/nums[i])
        return output
        