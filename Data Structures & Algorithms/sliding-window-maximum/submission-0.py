class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1

        heap_arr = []
        ret_list = []

        for i in range(r + 1):
            heap_arr.append([-1 * nums[i],i])

        heapq.heapify(heap_arr)

        while(r < len(nums)):
            while(heap_arr[0][1] < l):
                heapq.heappop(heap_arr)
            ret_list.append(-1 * heap_arr[0][0])
            r += 1
            l += 1
            if(r < len(nums)):
                heapq.heappush(heap_arr, [-1 * nums[r],r])

        return ret_list



        
        


        
        


