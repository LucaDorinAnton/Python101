# Lists and for loops


# declaring a list

lst = []
print(lst)
lst = [1,2,3,4,5]
print(lst)
lst = ["Apples", "Bananas", "Oranges", "Milk", "Cereals"]
print(lst)


# selecting parts from a list

print(lst[1])
print(lst[0])
print(lst[4])
print(lst[-1])
print(lst[-2])

#  other list operations

lst.append("Ice cream")
print(lst)
del(lst[0])
print(lst)
first = lst.pop()
print(first)
print(lst.pop())
print(lst)

#  for loops

lst = ["Apples", "Bananas", "Oranges", "Milk", "Cereals"]

for item in lst:
    print("I should buy some " + item)
    if item is "Oranges":
        print("Ew! I don't like Oranges!")


nums = [1,2,3,4,5,5,6,7,8,9,10]
nums = list(range(10))

for num in range(10):
    if num%2 is 0:
        print(str(num) + " is even!")
    else:
        print(str(num) + " is odd!") 
