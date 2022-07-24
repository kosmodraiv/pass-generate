import random

lower_case = "abcdefghijklmnpqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNPQRSTUVWXYZ"

number = "0123456789"

symbols = "@#$%*/\?"

Use_for = lower_case + upper_case + number + symbols

lenght_for_pass = 9

password = "".join(random.sample(Use_for, lenght_for_pass))

print("Password:", password)