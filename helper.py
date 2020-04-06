def maxUnitsAbleToPurchase(cash, price):
    if price == 0:
        return 0
    if cash >= price:
        return cash / price
    if cash < price:
        return 0