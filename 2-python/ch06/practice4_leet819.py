'''
LeetCode #819 [Most Common Word]

* collections.Counter.most_common()
'''

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Data Cleaning: Substitue non-alphanumeric characters to blank
        input_str = re.sub('[^\w]', ' ', paragraph.lower())
        # Data Cleaning: Get rid of banned word
        words_list = [word for word in input_str.split() if word not in banned]
        # Construct counter using word_list
        counter = collections.Counter(words_list)
        return counter.most_common(1)[0][0]
