# Leap_year

def leap_year(year):

    if (year % 400 == 0) and (year % 100 == 0):
        print(year," is a Leap year")
    elif (year % 4 == 0) and (year % 100 !=0):
            print(year," is a leap year. ")
    else:
            print(year, "is not a leap year.") 
    return year
year=int(input("Enter the year. "))  
(leap_year(year))  





