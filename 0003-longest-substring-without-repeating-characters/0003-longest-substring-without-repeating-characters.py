class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if(len(s)) == 0:
            return 0
        
        map = {}
        max_len = start = 0
        
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_len = max(max_len, i-start+1)
            map[s[i]] = i
            
        return max_len