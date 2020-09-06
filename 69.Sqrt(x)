def mySqrt(self, x):
        # bin search
        
        # find the lower bound by log
        y, b = x, 0
        while y:
            y = y >> 1
            b += 1
        
        lo, hi = min(2**((b-1)//2), 0), x 
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                lo = mid
            else:
                hi = mid - 1
                
        return lo

# A better way is by Newton's method
