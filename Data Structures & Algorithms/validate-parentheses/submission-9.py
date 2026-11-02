class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if len(stack) > 0:
                if(c in hashMap):
                    if(hashMap[c] == stack[-1]):
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False
        else:
            return True