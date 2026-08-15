class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(k>=len(s)):
            return len(s)
        max_length = 0
        charSet = set()
        for c in s:
            charSet.add(c)

        for c in charSet:
            l = 0
            r = 0
            err_count = 0
            while(r != len(s)):
                if s[r] != c:
                    err_count += 1
                while err_count > k:
                    if s[l] != c:
                        err_count -=1
                    l += 1
                max_length = max(max_length, r - l + 1)
                r += 1
        return max_length

