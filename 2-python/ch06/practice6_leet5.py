'''
LeetCode #5 [Longest Palindrome Substring]

* Dynamic Programming?
* Core Ideas:
(1) using odd and even windows at the same time
(2) expand the window while checking whether palindrome
(3) return palindrome early if there is nothing to check at the very begining
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # check whether palindrome and expand the window until palindrome condition broke
        def expand(left: int, right: int) -> str:
            # (1) left and right indices are within range and (2) check whether palindrome -- each side has the same character
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # length less than or equal to 1 / or itself is Palindrome
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # find the longest palindrome while moving window from the very left to the right
        for i in range(len(s) - 1):
            result = max(result, # keep the longest result among (1) previous result, and
                         expand(i, i + 1), # results from (2) odd, and
                         expand(i, i + 2), # (3) even windows
                         key=len)
        return result

class Solution: # Time Limit Exceeded
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(self, s: str) -> bool:
            return s == s[::-1]

        for i in range(len(s), 0, -1):
            min = 0
            max = min + i - 1
            while max < len(s):
                if checkPalindrome(self, s[min:max]):
                    return s[min:max]
                else:
                    min += 1
                    max = min+i