class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        return_arr = []
        for s in strs:
            representation = "".join(sorted(s))
            if representation in hashMap:
                hashMap[representation].append(s)
            else :
                hashMap[representation] = [s]
        for k in hashMap:
            return_arr.append(hashMap[k])
        return return_arr

        