'''
LeetCode #937 [Reorder Log Files]

* 2-dimensional List sorting
* use isdigit() rather re.search('[0-9]', str)
'''

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = list(), list()
        for i in range(len(logs)):
            element = logs[i].split(' ') # make list using each element
            if str(element[1]).isdigit(): # check whether digit-logs
                digits.append(' '.join(element))
            else: # string-logs
                letters.append([element[0], ' '.join(element[1:])])
        # sort letter list based on identifier than lexicographic-order
        # alternatively, letters.sort(key=lambda x: (x[1], x[0]))
        letters = sorted(sorted(letters, key=lambda x: x[0]), key=lambda x: x[1])
        # concatenate identifier and element
        letters = [' '.join(x) for x in letters]
        # The letter-logs come before all digit-logs.
        return letters + digits