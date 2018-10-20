def get_max_profit(stock_prices):

    max_profit = 0
    min_price = stock_prices[0]

    for next_price in stock_prices:
        min_price = min(min_price, next_price)
        max_profit = max(max_profit, next_price - min_price)

    return max_profit

test_stocks = [10, 7, 5, 8, 11, 9]
print(get_max_profit(test_stocks))
