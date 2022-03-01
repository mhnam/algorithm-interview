'''
LeetCode #49 [Group Anagrams]

* collections.defaultdict(default_type)
* sorted(string) will sort characters
* Sort - Quicksort, Timsort, Mergesort
'''
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # classification = dict()
        anagrams = collections.defaultdict(list) # better to assign as collections defaultdicts(list)

        for word in strs:
            char_list = sorted([char for char in word]) # sorted(word) is enough
            # if ''.join(char_list) in anagrams.keys():
            #     anagrams[''.join(char_list)].append(word)
            # else:
            #     anagrams[''.join(char_list)] = [word]
            anagrams[''.join(char_list)].append(word)
        return [anagrams[x] for x in anagrams.keys()] # alternatively list(anagrams.values())