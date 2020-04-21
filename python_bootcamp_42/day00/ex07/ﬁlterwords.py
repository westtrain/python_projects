import sys
import string
user_input = sys.argv
if len(user_input) < 3:
    print("ERROR")
elif user_input[1].isnumeric():
    print("ERROR")
else:
    str_input = user_input[1]
    words = str_input.split()
    int_input = int(user_input[2])
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    stripped = [x for x in stripped if len(x) > int_input]
    print(stripped)
