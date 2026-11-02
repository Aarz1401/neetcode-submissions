class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if(stack and c in hashMap):
                if(hashMap[c] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False
        else:
            return True