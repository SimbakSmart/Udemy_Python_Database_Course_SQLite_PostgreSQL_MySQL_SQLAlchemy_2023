try:
    salary = int(input("What is your salary? "))
except  Exception as ex:
    print("There was an error!"+ex)
else:
    if salary > 2000:
        print("You are eligible!")
    else:
        print("You are not eligible!")
finally:
    print("Thanks for using our calculcator!")