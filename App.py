import pandas as pd
import matplotlib.pyplot as plt

gdp_df = pd.read_csv("GDP2.csv", delimiter=",")#, skiprows=4)
china_df = gdp_df[gdp_df["Reference area"].str.contains("China", case=False, na=False)]
hungary_df = gdp_df[gdp_df["Reference area"] == "Hungary"]

total_assets = 500000000
total_liabilities = 200000000
shares_outstanding = 30000000
stock_price = 20
market_price = 8

book_value_of_equity = total_assets - total_liabilities
book_value_per_share = book_value_of_equity/shares_outstanding
price_to_book_value = market_price/book_value_per_share
market_value = stock_price * shares_outstanding


#print("Bool value of equity: $", "{:,}".format(book_value_of_equity).replace(',',' '),"\nBook value per share: $", book_value_per_share, "\nPrice-to-book value: $", price_to_book_value, "\nMarket value: $", "{:,}".format(market_value).replace(',', ' '))

#gdp_df = gdp_df.drop(columns=["Unnamed: 2"], errors="ignore")

print(gdp_df[["Reference area", "TIME_PERIOD", "OBS_VALUE"]])


'''
plt.plot(gdp_df["Year"], gdp_df["GDP"], marker="o", linestyle="-", color="b", label="GDP")
plt.xlabel("Год")
plt.ylabel("ВВП (млрд $)")
plt.legend()
plt.grid(True)
plt.show()
'''