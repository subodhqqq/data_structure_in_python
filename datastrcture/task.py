math=int(input("enter the math marks:"))
english=int(input("enter the English marks:"))
nepali=int(input("enter the Nepali marks:"))

if( math >=40 and english >=40 and nepali >=40):
    total = math+ english+nepali
    per=total/3
    if(per >=40 and per <50):
        print("student are pass in third division.")
    elif(per >=50 and per<60):
        print("student are pass in second division.")
    elif(per >=60 and per<80):
        print("student are pass in first division.")
    elif(per >=80 and per<100):
        print("student are pass in distion division.")
    else:
        print("plz enter the valid marsk")
else:
    print("the student are fail")
