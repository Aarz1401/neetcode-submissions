class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+','-','*','/']
        stack = []
        num1,num2 = 1 , 1
        for num in tokens:
            if num in operands:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = 0
                match(num):
                    case '+':
                        res = num1 + num2
                    case '-':
                        res = num1 - num2
                    case '*':
                        res = num1 * num2
                    case '/':
                        res = num1/num2
                stack.append(res)
            else:
                stack.append(int(num))
        return int(stack[0])


            
        