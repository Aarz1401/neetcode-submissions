class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = [0] * len(position)

        for i in range(len(position)):
            time[i] = (target-position[i]) / speed[i]
        
        time = [t for _, t in sorted(zip(position, time))]

        for t in time:
            while stack and (t >= stack[-1]):
                stack.pop()
            stack.append(t)
        return len(stack)
    
            
        

