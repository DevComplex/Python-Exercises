# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
    max_profit = 0

    N = len(prices)

    if N > 0:
        min_stock = prices[0]

        for i in range(1, N):
            max_profit = max(max_profit, prices[i] - min_stock)
            min_stock = min(min_stock, prices[i])

    return max_profit

