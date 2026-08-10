class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = ""
        for c in s:
            if c.isalnum():
                normalized_s += c.lower()
        reversed_s = ""
        for i in range(len(normalized_s)-1,-1,-1):
                reversed_s+=normalized_s[i]
        print(reversed_s)

        return normalized_s == reversed_s

        
        