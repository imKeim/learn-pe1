import os

def is_year_leap(year):
#
# Ваш код из предыдущей лабораторной работы
#

def days_in_month(year, month):
#
# Напишите новый код здесь.
#

def main():

    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")

if __name__ == "__main__":
    main()
