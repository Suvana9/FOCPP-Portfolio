print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

prices = []

for i in range(1, 5):
    while True:
        try:
          price = float(input(f"Enter Price of Pizza #{i}: "))
          if price <= 0:
                print("Invalid input! Please enter a number greater than 0.")
          else:
                prices.append(price)
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
cheapest = prices[0]
for price in prices:
    if price < cheapest:
        cheapest = price
original_total = sum(prices)
discounted_total =  original_total - min(prices)
discount_percentage = (min(prices) / original_total) * 100

print(
    f"Your Total Order is £{discounted_total:.2f}, "
    f"a fabulous discount of {round(discount_percentage)}%!"
)
