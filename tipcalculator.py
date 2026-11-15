print("Welcome to tip Calculator!!!!")
bill=float(input("what is the total bill $"))
tip=int(input("How much percen bill you want to give ?10,12,15 ="))
people=int(input("number of people to split bill"))

tip_as_percent=tip/100
tip_as_amount=bill*tip_as_percent
total_bill=bill+tip_as_amount
bill_per_person=total_bill/people
rounded_bill_per_person=round(bill_per_person,2)
print(f"calculated bill per person:${rounded_bill_per_person : .2f}")