def findDiagonalOrder(self, nums):
        bucket = collections.defaultdict(list)
        
        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                bucket[i+j].append(x)
                
        return [x for i in range(len(bucket)) for x in bucket[i][::-1]]
