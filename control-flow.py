# if else, elif, ternary if, while


# Making decisions

car_color = "red"

if car_color is "red":
    print("Wow, my car is really really fast!")

num = 5

if num > 6:
    print("My number is greater then 6")


# What to do in the other case?

if car_color is "red":
    print("Wow, my car is really really fast!")
else:
    print("My car is kinda slow...")

if num > 6:
    print("My number is greater then 6")
else:
    print("My number is smaller than or equal to 6...")

# Multiple options

if car_color is "red":
    print("Fast")
elif car_color is "yellow":
    print("Kinda fast")
else:
    print("Slow")

# Nesting conditions

num = 5

if num < 10:
    if num > 5:
        print("Grater than 5 but less than 10")
    else:
        print("Between 0 and 5")
else:
    print("Ten or more")

# Deciding on var assignment based on a condition

var = True if num > 10 else False

print(var)

# Loops - Repetition

num = 100
while num > 0:
    print(num)
    num = num - 1


num = 0

while num < 1000:
    num += 50
    print(num)

cals = 0
meals = 0
while cals < 2000:
    cals += 400
    meals += 1
    print("Today I've eaten " + str(meals) + " meals and about " + str(cals) + " calories!")
