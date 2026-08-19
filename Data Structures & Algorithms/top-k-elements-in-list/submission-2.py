class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        
        #hashMap is the frequency map
        min_heap = []
        for num, freq in hashMap.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return_list = []
        for freq,num in min_heap:
            return_list.append(num)

        return return_list


            

        