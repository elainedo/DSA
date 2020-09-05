def buy_stock_once(nums):
    lowest = float('inf')
    max_profit = 0.0
    for price in nums:
        max_profit = max(max_profit, price-lowest)
        lowest = min(lowest, price)
    return max_profit

print(buy_stock_once([310,315,275,295,260,270,290,230,255,250]))