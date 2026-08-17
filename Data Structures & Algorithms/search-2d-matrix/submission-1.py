class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            m_row = m // cols
            m_col = m % cols
            if matrix[m_row][m_col] < target:
                l = m + 1
            elif matrix[m_row][m_col] > target:
                r = m - 1
            else:
                return True
        return False


        