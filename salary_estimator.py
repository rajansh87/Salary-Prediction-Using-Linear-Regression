from sklearn.externals import joblib
model=joblib.load("salary_model.pk1")

print("\t\tWelcome to future tools")
print("---------------------------")


while True:
    print("Press 1: Salary Predict")
    print("Press 2: Predict new requirements")
    print("Press 3: Calculate score of current employee")
    print("Press 4: Classify score for current employee")
    print("Press 5: To Exit")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        exp=input("enter year of exp : ")
        prediction=(model.predict([[float(exp)]]))
        print("predicted salary is :",*prediction,sep=" ")
    elif ch==2:
        print("search new requirement")

    elif ch==3:
        print("cal")

    elif ch==4:
        print("classify")

    elif ch==5:
        exit()

    else:
        print("Invalide Choice")
