    year = int(input("What year is it? : "))
    if year % 100 == 0 or year % 400 == 0:
             print (str(year) + " is not a leap year.")
             continue
    elif year % 4 == 0 :
             print (str(year) + " is  a leap year.")  
             continue
    else :
        print (str(year) + " is not a leap year.")
        continue 





























