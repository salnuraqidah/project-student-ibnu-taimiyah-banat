score = int(input("Enter Your Score: "))

if score >= 85 and score <= 100:
    print("Grade is A")
elif score >= 70 and score < 85:
    print("Grade is B")
elif score >= 50 and score < 70:
    print("Grade is C")
else:
    print("Grade is D")