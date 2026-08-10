class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = ""
        for c in s:
            if c.isalnum():
                normalized_s += c.lower()
        return normalized_s == normalized_s[::-1]

        
        