class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we have to find what row of matrix target is in
        # take first element of every row and find upper and lower bound
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        down = rows - 1
        while(up <= down):
            mid = (up + down) // 2
            if matrix[mid][0] > target:
                down = mid - 1
            elif matrix[mid][0]< target:
                up = mid + 1
            else:
                return True
        target_row = (up + down) // 2
        left = 0
        right = cols - 1
        while(left <= right):
            mid = (left + right) // 2
            if matrix[target_row][mid] > target:
                right = mid - 1
            elif matrix[target_row][mid]< target:
                left = mid + 1
            else:
                return True
        
        return False







