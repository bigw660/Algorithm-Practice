def lastStoneWeightII(self, stones):
        # stupid brain teaser: basically, you need to try all combinations...
        values = set([stones[0], -stones[0]])
        
        for x in stones[1:]:
            temp1 = {y+x for y in values}
            temp2 = {y-x for y in values}
            temp1.update(temp2)
            values = temp1
            
        return min([x for x in values if x >= 0])
