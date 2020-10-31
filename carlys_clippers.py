hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#total_price variable
total_price = 0

#iterate throught the price list and add each price to total_price
for price in prices:
  total_price += price

#average_price
average_price = total_price / len(prices)

#print average_price
print("Average Haircut Price is: $" + str(average_price))

#new price cut by 5 dollars
new_prices = [price - 5 for price in prices]

#print new_price
print(list(new_prices))

#total_revenue from last week
total_revenue = 0

#calculate total_revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

#print out total_revenue
print("Total Revenue is: $" + str(total_revenue))

#average daily revenue
average_daily_revenue = total_revenue / 7
print("Daily Revenue of last week is: $" + str(average_daily_revenue))

#Haircuts that under 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30 ]


#print out cut under 30
print("These haircut styles are under 30: " + str(cuts_under_30))
