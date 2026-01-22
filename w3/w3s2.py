#act1
from erfa import atcc13

a = int(input("Enter a starting number"))
while a > 1:
    print (a)
    a -= 1

    print ("LIFT OFF!!!")
#act2
sum = 0
user_number = int(input("Enter a number"))
while user_number != 0:
    sum = sum + user_number
    user_number = int(input("Enter a number"))
print(sum)

# act3
password = ("python123")
guess = input("Enter password")
while guess != password:
  print("Incorrect password.")
  guess = input("Try Again.")

print("Correct Password. Welcome.")

#act4
secret = 17
guess = int(input("What is your guess?"))
while guess != secret:
    if guess > secret:
        print ("too high")
    elif guess < secret:
        print ("too low")
    guess = int(input("try again"))

print("Well Done")

#act5
choice = ""

while choice != "0":
    choice = input("1. Add \n2. Substraction \n0. Exit")
    if choice == "1":
        a, b = input("enter 2 numbers:").split()
        print(f"{a} plus {b} equals {int(a)+int(b)} " )
    elif choice == "2":
        a, b = input("Enter 2 numbers:").split()
        print(f"{a} minus {b} equals {int(a) - int(b)}")
print("Goodbye")

#act6
x = int(input("Insert a positive number"))
while True:
    if x <= 0:
        print("incorrect number")
        x = int(input("try again"))
    else:
        print(f"You entered: {x}")
        break

#act7
x = 0
marks = []
total = 0
while True:
    if x != -1:
        x = int(input("Insert a mark"))
        total += x
    else:
        print("-1 detected. Calculating sum NOW!\n---\n")
        print("Total entries: ", len(marks))
        print("Total score: ", total)
        print("Average: ", total/len(marks))
        break