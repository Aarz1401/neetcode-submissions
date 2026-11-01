class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(':')','[':']','{':'}'}

        for c in s:
            if(len(stack) > 0):
                if(stack[-1] in hashMap):
                    if(hashMap[stack[-1]] == c):
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        if(len(stack) > 0):
            return False
        else:
            return True
