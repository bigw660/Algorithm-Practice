def kthSmallest(self, matrix, k):
        # saddleback search
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        
        while lo < hi:
            mid = (lo+hi) // 2
    
            p, q, c = n-1, 0, 0 #(p,q) moving point, c: count
            # saddleback search
            while 0<=p and q < n:
                if matrix[p][q] > mid:
                    p -= 1
                else:
                    c += p + 1 # update number of elm < mid; 1 is bec p being an ind
                    q += 1
                    
            # binary search
            if c < k:
                lo = mid + 1
            else:
                hi = mid
            
        return lo
