import sys
user_input = sys.argv
if(user_input[1].isnumeric()):
    num = int(user_input[1])
    if(num == 0):
        sys.stdout.write("I'm Zero")
    elif(num % 2 == 0):
        sys.stdout.write("I'm Even")
    else:
        sys.stdout.write("I'm Odd")
else:
    sys.stdout.write("ERROR")
