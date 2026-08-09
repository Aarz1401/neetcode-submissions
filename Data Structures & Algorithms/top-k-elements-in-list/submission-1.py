class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else :
                hashMap[num] = 1
        arr =[]
        hashMap_sorted = dict(sorted(hashMap.items(),key = lambda p : p[1], reverse = True))
        count = 0
        for key, v in hashMap_sorted.items():
            if count >= k:
                return arr
            else :
                arr.append(key)
            count += 1
        return arr
            

        