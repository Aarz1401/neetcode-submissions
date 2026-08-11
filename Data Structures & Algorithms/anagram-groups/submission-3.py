class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnarr = []
        hashMap = {}
        for s in strs:
            refined_s = "".join(sorted(s))
            if(refined_s in hashMap):
                hashMap[refined_s].append(s)
            else :
                hashMap[refined_s] = [s]
        return list(hashMap.values())

            

        