class Solution:
    def climbStairs(self, n: int) -> int:
        o,t = 1,1
        
        for i in range(n-1):
            t1 = o
            o = o + t
            t = t1
            
        return o