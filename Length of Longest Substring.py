class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # keep track of characters already seen
        seen = []
        longest = 0

        for c in s:
            if c in seen:
                seen = seen[seen.index(c) + 1:]
            seen.append(c)
            longest = max(longest, len(seen))

        return longest

