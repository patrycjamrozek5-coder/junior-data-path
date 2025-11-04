# Program: Test score evaluation
# Description: Evaluates the test result (0-100) and print a descriptive rating.

result=int(input("Enter your test score in the field 0-100: "))

if result > 100:
    print('Error:Wrong number! The max number of points is 100')
    print('Try again')
elif 90 <= result <=100:
    print("Congratulations! Excellent rating")
elif 75 <= result <= 89:
    print("Good rating!")
elif 60 <= result <= 74:
    print("Satisfactory rating.")
else:
    print("I'm sorry. Next time will be better.")
    print("Unsatisfactory grade!")

#Example run:

#Enter your test score in the field 0–100: 150
#Error: Wrong number! The maximum score is 100.
#Try again.

#Enter your test score in the field 0–100: 84
#Good rating!


