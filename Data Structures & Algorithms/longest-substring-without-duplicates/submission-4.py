class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        hashSet = set()
        while(r != len(s)):
            curr_val = s[r]
            while(curr_val in hashSet):
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            max_length = max(max_length,r-l+1)
            r += 1
        return max_length
            
            


