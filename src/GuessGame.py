def date_guess():
    date = int(input(print("enter the birthday date")))
    while date != 8:
        print("incorrect guess")
        date = int(input(print("enter the birthday date")))
    if date == 8:
        print("correct guess")


date_guess()


