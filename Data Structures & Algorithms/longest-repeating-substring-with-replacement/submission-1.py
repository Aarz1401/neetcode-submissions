class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        # k is number of error tolerance
        charSet = set()
        for c in s:
            charSet.add(c)
        for c in charSet:
            l = 0
            r = 0 
            count = 0
            while(r!=len(s) and l!=len(s)): 
                if s[r] == c:
                    max_length = max(max_length, r - l + 1)
                    r += 1
                elif s[r]!=c and count < k:
                    count += 1
                    max_length = max(max_length, r - l + 1)
                    r += 1
                else: #count = k
                    if s[l]!=c :
                        count -= 1
                    l += 1
        return max_length



            




                



                



        