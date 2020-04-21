import string


def text_analyzer(s):
    upper = lower = space = punct = total = 0
    for char in s:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isspace():
            space += 1
        if char in string.punctuation:
            punct += 1
        total += 1
    print(f"The text contains {total} characters:")
    print()
    print(f"- {upper} upper letters")
    print()
    print(f"- {lower} lower letters")
    print()
    print(f"- {punct} punctuation marks")
    print()
    print(f"- {space} spaces")

