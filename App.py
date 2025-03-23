total_assets = 500000000
total_liabilities = 200000000
shares_outstanding = 30000000
stock_price = 20
market_price = 8

book_value_of_equity = total_assets - total_liabilities
book_value_per_share = book_value_of_equity/shares_outstanding
price_to_book_value = market_price/book_value_per_share
market_value = stock_price * shares_outstanding


print("Bool value of equity: $", "{:,}".format(book_value_of_equity).replace(',',' '),"\nBook value per share: $", book_value_per_share, "\nPrice-to-book value: $", price_to_book_value, "\nMarket value: $", "{:,}".format(market_value).replace(',', ' '))
