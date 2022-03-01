'''
LeetCode #125 [Valit Palindrome]

* Use re.findsub rather re.findall
* Slicing is the most fastest way to manage string
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_str = list(re.findsub('[^a-z0-9]', '', s.lower()))
        return list_str == list_str[::-1]