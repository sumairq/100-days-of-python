print("Welcome to the tip Calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
num_people = input("How many people to split the bill?")

bill_int = int(bill)
tip_int = int(tip)

total_tip = (tip_int/100) * bill_int
total_bill = bill_int + total_tip
amount_to_each = total_bill / int(num_people) 

print(f"Each person should pay: ${round(amount_to_each, 2)}")
      