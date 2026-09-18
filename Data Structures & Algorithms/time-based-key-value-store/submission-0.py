class TimeMap:

    def __init__(self):
        # Maps key -> list of [timestamp, value] pairs
        self.timeMap = {}       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        pairs = self.timeMap[key]
        
        # binary search
        left, right = 0, len(pairs) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1] #valid candidate
                left = mid + 1
            else:
                # The current timestamp is too large, search the left half
                right = mid - 1
                
        return result
