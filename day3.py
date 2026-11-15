# if else statement and elif statement as well as multiple else statement

age=int(input("enter your age please ?? "))
if age>=18:
    print("you are allowed to vote")
else:
    print("you are below 18!!")


marks=int(input("please enter your marks"))
if marks>90:
    print("Grade A")
elif marks>80:
    print("Grade B")
elif marks>70:
    print("grade C")
elif marks>60:
    print("grade D")
else:
    print("You need to do hardwork")

if marks>30 and age >18:
    print("your are eligible candidate")
else :
    print("not eligible")
