# Comments variables, types, expressions,basic IO

# This is a comment

'''
This is a multiline comment.
It's a comment which spans multiple lines.
Neat, right?
'''

print(10)
print('a')
print(12.567)
print("Some text")
print(True)
print(False)
print(5 + 2)
print(1000/6)

var = 10

print(var)

txt = "This is a string"
print(txt)

# You can reassign variables

var1 = 10
print(var1)
var1 = 20
print(var1)
var1= "Now I am a string"
print(var1)
var1 = False
print("The value of var1 is now: ", var1)
var1 = 1
print(var1, var1 + 1, var1 + 3, var1 + 1000000)

# How to get input from the keyboard

inp = input("Please enter your input: > ")

num = int(inp)

print(inp + "1", num + 1)
