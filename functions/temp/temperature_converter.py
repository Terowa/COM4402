def cel_to_fahr ():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = celsius * (9/5) + 32
    print(fahrenheit)
    return fahrenheit

def fahr_to_cel ():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print(celsius)
    return celsius

fahr_to_cel()

