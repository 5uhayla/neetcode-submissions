class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curNum = 0
        while curNum < len(prices):
            nextNum = curNum + 1
            while nextNum < len(prices):
                if (prices[nextNum] - prices[curNum]) > profit:
                    profit = prices[nextNum] - prices[curNum]
                nextNum += 1
            curNum += 1
        return profit