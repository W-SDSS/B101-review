"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

initial = float(input("An initial debt: "))
r = float(input("The monthly interest rate: "))
payment = float(input("The monthly payment: "))

r = r/100
debt = initial
total_interest = 0
month = 0

while debt > 0:
    interest = debt*r
    total_interest = total_interest + interest
    debt = debt + interest
    debt = debt - payment
    month = month + 1

print("debt will have paid in", month, "month")
print("debt will have paid", round(total_interest, 2), "in interest.")