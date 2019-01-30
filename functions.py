# ---------------------------------------------------------------------

print("Lyrics for 'My Name Is' - Eminem")

print("\n-------------------------------------\n")

print("Hi! My name is (what?)")
print("My name is (who?)")
print("My name is")
print("Slim Shady")
print("Hi! My name is (huh?)")
print("My name is (what?)")
print("My name is")
print("Slim Shady")
print()
print("Hi! My name is (what?)")
print("My name is (who?)")
print("My name is")
print("Slim Shady")
print("Hi! My name is (huh?)")
print("My name is (what?)")
print("My name is")
print("Slim Shady")


print("\n-------------------------------------\n")
print("rest of the song...")
print("\n-------------------------------------\n")

print("Hi! My name is (what?)")
print("My name is (who?)")
print("My name is")
print("Slim Shady")
print("Hi! My name is (huh?)")
print("My name is (what?)")
print("My name is")
print("Slim Shady")
print()
print("Hi! My name is (what?)")
print("My name is (who?)")
print("My name is")
print("Slim Shady")
print("Hi! My name is (huh?)")
print("My name is (what?)")
print("My name is")
print("Slim Shady")

print("\n-------------------------------------\n")

lst = [2, 4, 6, 8]

total = 0
count = 0

for item in lst:
	count += 1
	total += item

print("Average is: " + str(total/count))

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for item in lst:
	count += 1
	total += item

print("Average is: " + str(total/count))


# ---------------------------------------------------------------------


# defining functions

def chorus():
    print("Hi! My name is (what?)")
    print("My name is (who?)")
    print("My name is")
    print("Slim Shady")
    print("Hi! My name is (huh?)")
    print("My name is (what?)")
    print("My name is")
    print("Slim Shady")
    print()
    print("Hi! My name is (what?)")
    print("My name is (who?)")
    print("My name is")
    print("Slim Shady")
    print("Hi! My name is (huh?)")
    print("My name is (what?)")
    print("My name is")
    print("Slim Shady")

# calling functions

chorus()
print("\nRest of the song...\n")
chorus()

# Using parameters/arguments and return values

def avg(lst):
    total = 0
    count = 0
    for item in lst:
    	count += 1
    	total += item
    return total/count

lst1 = list(range(10))
lst2 = list(range(100))
list3 = list(range(1000000))

avg1 = avg(lst1)
avg2 = avg(lst2)
avg3 = avg(lst3)

print("Avg of lst1 is " + avg1)
print("Avg of lst2 is " + avg2)
print("Avg of lst3 is " + avg3)
