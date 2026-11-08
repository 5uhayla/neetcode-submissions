class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curNum = 0
        while curNum < len(prices):
            print(f"curNum: {curNum}")
            nextNum = curNum + 1
            while nextNum < len(prices):
                print(f"nextNum: {nextNum}")
                if (prices[nextNum] - prices[curNum]) > profit:
                    profit = prices[nextNum] - prices[curNum]
                    print(f"new profit: {profit}")
                nextNum += 1
            curNum += 1
        return profit