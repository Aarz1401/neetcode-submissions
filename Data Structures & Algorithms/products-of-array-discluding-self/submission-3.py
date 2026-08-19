class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        count_zeroes = 0
        output =[0] * len(nums)
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                count_zeroes +=1
        
        if count_zeroes > 1:
            return output
        else:
            for i,num in enumerate(nums):
                if count_zeroes == 1:
                    if num == 0:
                        output[i] = int(total_product)
                    else:
                        continue
                else:
                    if num != 0:
                        output[i] = int(total_product / num)
                    else:
                        output[i] = int(total_product)
        
        return output
                    


