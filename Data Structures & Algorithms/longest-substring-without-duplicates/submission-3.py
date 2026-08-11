class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        max_length = 0
        myset = set()
        while(r!= len(s)):
            if(not(s[r] in myset)):
                myset.add(s[r])
                r += 1
                max_length = max(r-l,max_length)
            else :
                myset.remove(s[l])
                l += 1
        return max_length
        


        