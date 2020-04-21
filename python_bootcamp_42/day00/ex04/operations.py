import sys


user_input = sys.argv
if len(user_input) > 3:
    print("too many arguments")
    print()
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
elif len(user_input) < 2:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
elif user_input[1].isnumeric() and user_input[2].isnumeric():
    x = int(user_input[1])
    y = int(user_input[2])
    add = x + y
    diff = x - y
    prod = x * y
    print(f"Sum:          {add}")
    print(f"Difference:   {diff}")
    print(f"Product:      {prod}")
    if y == 0:
        print("Quotient:     ERROR (modulo by zero)")
        print("Remainder:    ERROR (modulo by zero)")
    else:
        remain = x % y
        quot = x / y
        print(f"Quotient:     {quot}")
        print(f"Remainder:    {remain}")
else:
    print("only numbers")
    print()
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
