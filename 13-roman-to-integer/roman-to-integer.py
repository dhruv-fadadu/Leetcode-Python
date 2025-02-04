class Solution:
    def romanToInt(self, s: str) -> int:
        store = {'I': 1, 'V': 5, 'X': 10, 'L': 50 ,'C': 100, 'D': 500, 'M':1000}
        n = len(s)
        ans = 0
        
        i = 0
        while i < n:
            if i<n-1 and store[s[i]] < store[s[i+1]]:
                ans += store[s[i+1]] - store[s[i]]
                i += 2
            else:
                ans += store[s[i]]
                i += 1

        return ans