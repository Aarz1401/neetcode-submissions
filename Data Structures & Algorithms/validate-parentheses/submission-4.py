class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap = {'{':'}','(':')','[':']'}
        for b in s:
            if len(stack) == 0:
                stack.append(b)
            else :
                if stack[-1] in myMap:
                    if myMap[stack[-1]] == b:
                        stack.pop()
                    else:
                        stack.append(b)
                else:
                    stack.append(b)
                
              
        if stack == []:
            return True
        else:
            return False