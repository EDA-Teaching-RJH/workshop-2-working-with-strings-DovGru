score = int(input("What was your score?: "))

if score >= 90 and score <= 100:
    print("You Scored a 1st")
elif score >= 80 and score <= 89:
    print("You scored a 2:1")
elif score >= 70 and score <= 79:
    print("You scored a 2:2")
elif score >= 60 and score <= 69:
    print("You scored a 3rd")
else:
    print("failed")