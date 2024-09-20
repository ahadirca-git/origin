import random2
start = int(input("Use Start number: "))
end = int(input("Use End number: "))
if start < end:
    r1 = random2.randint (start, end)
    print("Random number between start and end is % s" % (r1))
else:
    r1 = random2.randint(end, start)
    print("Random number between start and end is % s" % (r1))