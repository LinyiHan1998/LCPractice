class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        n, m = binaryMatrix.dimensions()
        
        def valid(j: int): -> bool              # Check the validity of a column given its indice
            i = 0
            while i < n:
                if binaryMatrix.get(i, j):
                    return True
                i += 1
            return False
        
        if not valid(m-1):                      # If the last column is not valid all columns are 0
            return -1
        
        lo, hi = 0, m - 1                       # Binary search
        while lo <= hi:
            mid = hi + (lo - hi)//2
            if valid(mid):
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo                               # Return low, we are looking for a left bound
    