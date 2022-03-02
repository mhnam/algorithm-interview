'''
LeetCode 121 [Best Time to Buy and Sell Stock]

* Kadane's Algorithm
'''
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, sys.maxsize

        for price in prices:
            # min_price get updated as time goes by
            min_price = min(min_price, price)

            # check whether current price can generate the largest profit from the previous lowest price
            profit = max(profit, price - min_price)

        # Similar to Brute-Force Algorithm
        # for i in range(len(prices)):
        #     profit = max(profit, max(prices[i+1:])-prices[i])

        return profit
