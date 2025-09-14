# Strings in Python
# print(len("23234"))
# print("234" + "234")

#Integers in python
# print(1+2+3)

#Large Numbers in Python
# print(234_456_667)

#Floating Point Numbers:
# print(23.3456)

#Boolean 
# True or False

# len("12344")
# print(type(1234))

#Tip Calculator:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))  

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
# print(type(bill))
# print(type(tip))
