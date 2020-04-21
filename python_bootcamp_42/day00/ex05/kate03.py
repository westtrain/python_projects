import sys
phrase = "The right format"
if len(phrase) < 42:
    need_fill = 42 - len(phrase)
    while need_fill > 0:
        sys.stdout.write("-")
        need_fill -= 1
    sys.stdout.write(phrase)
