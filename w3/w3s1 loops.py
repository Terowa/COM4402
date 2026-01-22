# act1
for i in range(11):
    print ("hello")

#act2
n = int(input("Insert a number"))
sum = 0
for i in range (0,n+1):
    sum = sum ++i
print (sum)

#act3
x = int(input("insert a number"))
for i in range (1,11):
    solution = i*x
    print (solution)

#act4
sent = input("type a sentence")
letters = 0
for i in sent:
    if i != " ":
        letters = letters + 1

print (f"there are {letters} letters in your sentence.")

# act5
marks = int(input("how many marks will you input?"))
highest = 0
for i in range(1, marks + 1):
    mark = int(input("enter the next mark"))
    if highest < mark:
        highest = mark

print(f"the highest mark is {highest}")

#act6
total_scores = int(input("how many marks will you input"))
marks = []

for i in range (total_scores):
    mark = int(input(f"Enter mark {i + 1} of {total_scores}: "))
    marks.append(mark)

pass_counter = 0
for mark in marks:
    if mark >= 40:
        print (mark)
        pass_counter += 1

print (f"{pass_counter} students passed.")

#act7
word = str(input("Enter a word"))
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print (reversed_word)

#act8
names = int(input("How many names will you enter?"))
names_list = []
name_count = 0
for i in range (names):
    name = input(f"what is name {i+1} of {names}")
    names_list.append(name)
letter = input("What letter do you seek?")
for i in names_list:
    for char in i:
        if char.lower == letter.lower:
            name_count += 1
            break
print (name_count)

#act9



