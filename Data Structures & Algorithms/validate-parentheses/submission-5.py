class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap = {']':'[',')':'(','}':'{'}
        for c in s:
            if c in myMap and stack != []:
                if stack[-1] == myMap[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
            
            print(stack)
        
        if stack == []:
            return True
        else:
            return False