class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #3
        cols = len(matrix[0]) #4

        top,bottom = 0,rows-1

        while top<=bottom:
            mid = (top+bottom)//2

            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                break
        
        l,r = 0,cols-1

        while l<=r:
            m = (l+r)//2
            if target < matrix[mid][m]:
                r=m-1
            elif target > matrix[mid][m]:
                l = m+1
            else:
                return True
        return False
        