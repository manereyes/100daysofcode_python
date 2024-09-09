### Tip Calculator ###

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip do you want to give? (10, 12, 15, 20...) = "))
total_bill = (bill*tip/100)+bill

ppl = int(input("How many people to split the bill? "))
split_bill = round(total_bill/ppl, 2)
print(f"Each person should pay ${split_bill}")