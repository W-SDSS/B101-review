"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

P = float(input("The number of an initial investment: "))
r = float(input("The annual interest rate (%): "))
time = float(input("The length of time:"))
unit = str(input("What is the unit for time (year, month, day):"))

r = r/100

if unit == "year":
  t = time
elif unit == "month":
  t = time/12
elif unit == "day":
  t = time/365
else:
  print("invalid value")

I = P*r*t

print(I)