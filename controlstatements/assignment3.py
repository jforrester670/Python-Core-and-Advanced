m,p,c = [int(x) for x in input("Enter marks for Math, Physics, and Chemistry: ").split()]
if m<35 or p<35 or c<35:
    print("Student failed an exam")
else:
    average = (m+p+c)/3
    if average <= 59:
        print("Student's grade is a C")
    elif average > 59 and average <= 69:
        print("Student's grade is a B")
    else:
        print("Student's grade is an A")