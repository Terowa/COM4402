age = int(input("Enter your age: "))
if age < 5:
    ticket = "Free entry"
elif age < 18:
    ticket = "Child Ticket"
elif age < 65:
    ticket = "Adult Ticket"
else:
    ticket = "Senior Ticket"
print (f"you have purchased a {ticket}")