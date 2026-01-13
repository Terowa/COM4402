#act1
message = "out"

def greet():
 message = "Hello from the function"
 print(message)


greet()
print(message)

#act2


#act3

def area_of_rectangle(w, h):
    area = w*h
    return area

x = area_of_rectangle(4,7)
print (f"Area is {x}")

#act4

def calculate_tax(amount, rate):
 return amount * rate

returns = calculate_tax(50, 0.2)
print(returns)
#version 2 allows for the dynamic change of the value of rate within the function

#act5

def apply_discount(price):
 if price > 100:
     discount = 10
     final_price = price - discount
     return final_price
 else:
    return price
p = float(input("Enter price: "))

result = apply_discount(p)
print("Final price:", result)

#act6
def show_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    return choice


def deposit(balance):
    amount = float(input("Amount to deposit: "))
    if amount < 0:
        print(f"{amount} cant be dopisited.")
    else:
        balance = balance + amount
        print(f"Your current balance is {balance}")
        return balance


def withdraw(balance):
    amount = float(input("Amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance = balance - amount
        print(f"Your current balance is {balance}")
        return balance


balance1 = 0
while True:
    user_choice = show_menu()
    match user_choice:
        case 1:
            balance1 = deposit(balance1)
        case 2:
            balance1 = withdraw(balance1)
        case 0:
            break

#act7

def add_mark(mark, total):

    total = total + mark
    return total

mark1 = int(input("Enter mark 1: "))
total = add_mark(mark1)
mark2 = int(input("Enter mark 2: "))
total = add_mark(mark2)

print("Total:", total)