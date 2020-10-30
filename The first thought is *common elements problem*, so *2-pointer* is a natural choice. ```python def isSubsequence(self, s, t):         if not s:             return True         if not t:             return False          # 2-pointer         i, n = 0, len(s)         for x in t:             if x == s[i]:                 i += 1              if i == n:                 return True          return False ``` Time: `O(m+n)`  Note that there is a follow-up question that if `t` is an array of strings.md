The first thought is *common elements problem*, so *2-pointer* is a natural choice.
```python
def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False

        # 2-pointer
        i, n = 0, len(s)
        for x in t:
            if x == s[i]:
                i += 1

            if i == n:
                return True

        return False
```
Time: `O(m+n)`

Note that there is a follow-up question that if `t` is an array of strings.
