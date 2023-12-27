print("input bangla marks: ")
bangla = int(input())

if bangla >= 91 and bangla <100:
    print("A+")
elif bangla >=81 and bangla <=90:
    print("A")
elif bangla >= 71 and bangla <=80:
    print("B")
elif bangla >= 61 and bangla <= 70:
    print("C")
elif bangla >= 41 and bangla <=60:
    print("D")
else:
    print("F")

# english marks
print("input english marks: ")
english = int(input())

if english >= 91 and english <=100:
    print("A+")
elif english >=81 and english <=90:
    print("A")
elif english >= 71 and english <=80:
    print("B")
elif english >= 61 and english <= 70:
    print("C")
elif english >= 41 and english <= 60:
    print("D")
else:
    print("F")
# science marks
print("input science marks:")
science = int(input())

if science >= 91 and science <=100:
    print("A+")
elif science >=81 and science <=90:
    print("A")
elif science >= 71 and science <=80:
    print("B")
elif science >= 61 and science <= 70:
    print("C")
elif science >= 41 and science <= 60:
    print("D")
else:
    print("F")
# mathmarks
print("input math marks: ")
math = int(input())

if math >= 91 and math <=100:
    print("A+")
elif math >=81 and math <=90:
    print("A")
elif math >= 71 and math <=80:
    print("B")
elif math >= 61 and math <= 70:
    print("C")
elif math >= 41 and math <= 60:
    print("D")
else:
    print("F")

average = int((bangla + english + math + science) / 4)
print("Average:", average)
