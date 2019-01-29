import random
import string

n = input("How many passwords would you like to print? >")

l = input("How long should the passwords be? > ")

n = int(n)

l = int(l)

chars = string.ascii_letters + string.digits + "!@#$%^&*"
print("Here are your passwords:\n")

for i in range(n):

    pwd = "".join(random.choice(chars) for i in range(l))
    print(pwd)
