import random
lower = "abcdefghijklmnopqrtsuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*(){}_\/?]["

all = lower + upper + numbers + symbol
length = 9
password = "".join(random.sample(all,length))
print(" Welcome to Password Generator, Your new password is :", password)