class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap ={')':'(',']':'[','}':'{'}

        for c in s:
            if stack and c in myMap:
                if(myMap[c] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if(stack):
            return False
        else:
            return True