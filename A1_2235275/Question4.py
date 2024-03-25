####Question4#######

default_string = "I like Python"
n = 4

if n < 0 or n >= len(default_string):
    result = ""
else:
    result = default_string[n:]

print(result)
