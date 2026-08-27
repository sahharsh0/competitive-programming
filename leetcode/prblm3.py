
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chmap= {}
        l = 0
        ml= 0
        for right, char in enumerate(s):
            if char in chmap and chmap[char] >= l:
                l = chmap[char] + 1
            
            chmap[char] = right
            ml = max(ml, right - l + 1)
            
        return ml
print(Solution().lengthOfLongestSubstring("abcabcbb"))