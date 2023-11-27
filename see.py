def your_age(current_year, year_of_birth):
    age = current_year - year_of_birth
    if age >= 18:
        print(f"your age is {age} and you are eligible to vote")
    else:
        print(f"your age is {age} and you are not eligible to vote")
current_year = int(input("Enter current year: "))
birth_year = int(input("enter your year of birth: "))
your_age(current_year, birth_year)