print("input bangla marks: ")
bangla = int(input())

if bangla>100 or bangla<0:
    print("Marks have to be between 0 and 100 ")
    exit()


# english marks
print("input english marks: ")
english = int(input())

if english >100 or english <0:
  print("Marks have to be between 0 and 100")
  exit()

# science marks
print("input science marks:")
science = int(input())

if science >100 or science <0:
    print("Marks have to be between 0 and 100")
    exit()
# mathmarks
print("input math marks: ")
math = int(input())

if math > 100 or math <0:
    print("Marks have to be between 0 and 100")


average = int((bangla + english + math + science) / 4)
if average >=91 and average <= 100:
    print("Obatined Grade: A+")
elif average>=81 and average <=90:
    print("Obtained Grade: A")
elif average>=71 and average<=80:
    print("Obtained GradeB")
elif average>=61 and average<=70:
    print("Obtained Grade: C")
elif average>=41 and average<=60:
    print("Obtained Grade: D")
else:
    print("obtained Grade: F")
