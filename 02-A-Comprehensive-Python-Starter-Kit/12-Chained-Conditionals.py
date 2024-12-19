
print("Welcome to Mortage Calculator")

salary = int(input("What is your salary ? "))



if salary >= 2000:
    print("Yoare eligible for mortage!")

    credit_score =int(input("What is your credit score? "))

    if(credit_score >800):
        print("Inerest rate : 4%")
    elif credit_score >750 :  
          print("Interes rate : 6%")
    else:
        print("Interes rate : 8%")

else:
    print("Sorry, you are not elegible")