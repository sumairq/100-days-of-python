print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))



total_tip = (tip/100) * bill
total_bill = bill + total_tip
amount_per_person = round(total_bill / int(num_people), 2)

print(f"Each person should pay: ${amount_per_person}")
      