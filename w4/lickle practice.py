#lists
nums = [3, 6, 9, 12]
print(nums[0] , nums[3])

colours = ["red", "blue", "black", "white"]
colours.append(["purple"])

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
fruits[1] = "mango"
print(fruits[1])

#
person = {
    "name": "same",
    "city": "London",
}

person["age"] = 25
person["city"] = "Bolton"
new_age = int(input("Enter your true age: "))
person["age"] = new_age
print(person)