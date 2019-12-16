class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        d = {}
        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]]+1
            else:
                max_len = max(max_len, i-start+1)
            d[s[i]] = i
        return (max_len)
    
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))