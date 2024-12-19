
print("Welcome to Mortage Calculator")

salary = int(input("What is your salary ? "))
rate=0


if salary >= 2000:
    print("You are eligible for mortage!")

    credit_score =int(input("What is your credit score? "))

    if(credit_score >800):
        rate=4
        print("Inerest rate : 4%")
    elif credit_score >750 :  
          rate=8
          print("Interes rate : 6%")
    else:
        rate=8
        print("Interes rate : 8%")

    disability = input("Do you have any disability ? ")
    if disability=="Y":
        rate-=2

        print(f"Final Interes rate : {rate}%")
         

else:
    print("Sorry, you are not elegible")