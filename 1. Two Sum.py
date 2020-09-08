def twoSum(self, nums, target):
        # hash table
        
        seen = dict()        
        for i, x in enumerate(nums):
            if target - x in seen:
                return([seen[target-x], i])
            else:
                seen[x] = i
