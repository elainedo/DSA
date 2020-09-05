def buy_stock_twice(nums):
    max_profit_arr = []
    max_profit = 0
    lowest = float('inf')
    for price in nums:
        max_profit = max(max_profit, price-lowest)
        max_profit_arr.append(max_profit)
        lowest = min(lowest, price)

    def buy_stock_twice_helper(nums):
        max_profit_arr = []
        max_profit = 0
        highest = 0
        for price in reversed(nums):
            max_profit = max(max_profit, highest-price)
            max_profit_arr.insert(0, max_profit)
            highest = max(highest, price)
        return max_profit_arr
    
    reverse_profit = buy_stock_twice_helper(nums)

    result = 0
    for i in range(0, len(nums)):
        result = max(result, max_profit_arr[i] + reverse_profit[i])
    
    return result


print(buy_stock_twice([12,11,13,9,12,8,14,13,15]))