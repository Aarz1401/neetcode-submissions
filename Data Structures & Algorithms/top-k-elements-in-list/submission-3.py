class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        numMap = {}
        return_arr = []
        for n in nums:
            if (n in numMap):
                numMap[n] += 1
            else:
                numMap[n] = 1
    
        for key,v in numMap.items():
            if(len(min_heap) < k):
                heapq.heappush(min_heap,(v,key))
            else:
                heapq.heappush(min_heap,(v,key))
                heapq.heappop(min_heap)
        
        for key,v in min_heap:
            return_arr.append(v)
        
        return return_arr

            

        
        
