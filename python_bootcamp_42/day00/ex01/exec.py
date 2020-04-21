import sys
str = sys.argv
i = len(str[1]) - 1
while(i >= 0):
    if(str[1][i].isupper()):
        sys.stdout.write(str[1][i].lower())
    else:
        sys.stdout.write(str[1][i].upper())
    i -= 1
