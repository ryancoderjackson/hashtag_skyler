#1 Dollarizer
def dollarizer(word):
    return word.replace("s","$")

crush = "skyler"
dollar = dollarizer(crush)
print(f"1.Dollarizer: {dollar}")


#2 Eurizer
def eurizer(word):
    return word.replace("e","€")

euro = eurizer(crush)
print(f"2.Eurizer: {euro}")


#3 Replacer
def replacer(word, char1, char2):
    return word.replace(char1, char2)

SkyRy = "SkyRy"
char1 = "y"
char2 = "#"

output_word = replacer(SkyRy, char1, char2)
print(f"3.Replacer: {output_word}")


#4 Wonky Text
def wonky_text(word):
    return word.replace("l","£")

wonky = eurizer(dollar)
wonkytext = wonky_text(wonky)
print(f"4.Wonky Text: {wonkytext}")


#5 Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = float(input("What is the tempurature in Celsius? "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"5.Celsius to Fahrenheit: {celsius_temp}°C is equal to {fahrenheit_temp}°F")


#6 Age in Days
def age_in_days(years):
    days = years * 365
    return days

years = int(input("Enter your age as a number: "))
days = age_in_days(years)
print(f"6.Age in Days: If you are {years} years old, then you are approximately {days} days old")


#7 Simple Interest
def simple_interest(principle, rate, time):
    si = (principle * rate * time)
    return si

principle = float(input("What is the principle amount of your loan? "))
rate = float(input("Enter the rate of interest as a decimal: "))
time = float(input("Enter the time in years on your loan as a number: "))
si = simple_interest(principle, rate, time)
print(f"7.Simple Interest: {si}")


#8 Plan Finances
def plan_finances(principle, desired_final_amount):
    si_result = si / 100
    final_amount = principle + si_result
    if final_amount == desired_final_amount:
        return True
    else:
        return False

#Test Results For Function
#principle = 1000, rate = 5, time = 3
#For the result to be true, desired final amount = 1150. Any other number makes the result false.
desired_final_amount = float(input(f"With the simple interest being {si}, Now enter the desired final amount: "))
result = plan_finances(principle, desired_final_amount)
print(f"8.Plan Finances: {result}")


print("")


print("9.shapes.py tests:")
def area_of_rectangle(a, b):
    return a * b
#The area of a rectangle
#a = int(input("Enter the length of the rectangle "))
#b = int(input("Enter the width of the rectangle "))
#print(f"The area of the rectangle is {area_of_rectangle(a, b)}")


def square_perimeter(g):
    return 4 * g
#the result of g is the area of the square
g = int(input("Enter the side length of the square "))
print(f"10.Square Perimeter: The perimeter of the square is {square_perimeter(g)}")


def area_of_circle(c, d):
    return d * c**2
#circle_details calculates the circumference of circle
def circle_details(c, d):
    return 2 * d * c
#The area of a circle
c = int(input("Enter the radius of the circle "))
import math
d = math.pi
print(f"11.Circle Details: The area of the circle is {area_of_circle(c, d)}")
print(f"11.Circle Details: The circumference of the circle is {circle_details(c, d)}")


def area_of_triangle(e, f):
    return f * e / 2
#The area of a triangle
#e = int(input("Enter the base of the triangle "))
#f = int(input("Enter the height of the triangle "))


def geometry (square_side, circumference):
    perimiter = square_perimeter(square_side)
    radius = int(input("Enter the radius of the circle "))
    pi = math.pi
    circumference = circle_details(radius, pi)
    area = area_of_circle(radius, pi)

    if perimiter > circumference:
        print("12.Geometry: The square's perimeter is larger than the circle's circumference")
    elif perimiter < circumference:
        print("12.Geometry: The square's perimeter is smaller than the circle's circumference") 
    else:
        print("12.Geometry: The square's perimeter and the circle's circumfererence are the same")
    
    if square_side > area:
        print("12.Geometry: The square's area is larger than the circle's area")
    elif square_side < area:
        print("12.Geometry: The square's area is smaller than the circle's area")
    else:
        print("12.Geometry: The square's area and the circle's area are the same")
side = int(input("Enter the side length of the square "))
circle = int(input("What is the circumference of the circle "))
print(geometry(side, circle))