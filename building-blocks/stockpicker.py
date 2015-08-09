def stockpicker(stock_prices):
    best = 0
    for i in range(len(stock_prices)):
        count = 1
        while count + i < len(stock_prices):
            if stock_prices[i] < stock_prices[i + count]:
                profit = stock_prices[i + count] - stock_prices[i]
                if profit > best:
                    best = profit
                    buy = i
                    sell = i + count
            count += 1
    print "You should buy on day %d and sell on day %d for a profit of %d." %(buy, sell, best)
