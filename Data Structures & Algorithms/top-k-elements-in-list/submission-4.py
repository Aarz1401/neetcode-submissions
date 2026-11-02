class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = [] # has frequency, num pairs
        numsMap = {} # key is num, value is frequency
        ret_arr = []
        for num in nums:
            if(num in numsMap):
                numsMap[num] += 1
            else:
                numsMap[num] = 1
        
        for key,v in numsMap.items():
            if(len(min_heap) < k):
                heapq.heappush(min_heap,(v,key))
            else:
                heapq.heappush(min_heap,(v,key))
                heapq.heappop(min_heap)
        
        # final iteration
        for f,num in min_heap:
            ret_arr.append(num)

        return ret_arr        

            