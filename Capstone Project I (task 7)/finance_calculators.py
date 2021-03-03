
import math

finance = input('''Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment \t- to calculate the amount of interest you'll earn on interest
bond \t\t- to calculate the amount you'll have to pay on a home loan\n:''')
if (finance == "investment") or (finance == "INVESTMENT") or (finance == "Investment"):

# finance is used as a variable to store the inputted value of the user.
# user needs to enter investment or bond based on:
# 'finance' is equal to (investment or Investments or INVESTMENTS) (inputted value need to meet at least one criteria)
# 'finance' is equal to (bond or Bond or BOND) (inputted value need to need to meet at least one criteria)
# If all else fails the else statement right below will print out (Please enter correct wording)

#******************** Investment ********************
    
    deposit = int(input("The amount of money you are depositing: R"))
    percentage = int(input('''The interest rate (as a percentage).\nOnly the number of the interest rate should be entered — no need for the symbol %: '''))
    years = int(input("The number of years they plan on investing for: "))
    finance = input("Do you want 'simple' or 'compound' interest: ")

# When inputted value matches if statement of investment then
# 'deposit' statement is printed and used and a variable to store inputted statement as a whole value inputted by the user 
# 'percentage' statement is printed and used and a variable to store inputted statement as a whole value of the integer
# 'years' statement is printed and used and a variable to store inputted statement as a whole value of the interger
# 'finance' is printed and then been over writen and used and a variable to store inputted statement as a string:
# User need to type either 'simple' or 'compound'


#*** Simple and compound calculation for investment ***
    
if finance == "simple":
    r = percentage / 100
    P = deposit
    t = years
    A = (P*math.pow((1+r),t))
    print("Simple interest will be R",A)
elif finance == "compound":
    r = percentage / 100
    P = deposit
    t = years
    A =(P*(1+r*t))
    print("Compound interest will be R",A)

#if 'finance' is equal to 'simple' the following statement will follow for calculation
# r is equal to 'percentage' devided by 100
# P is equal to 'deposit'
# t is equal to 'years'
# above will be substituted in the formula based on the ****investment**** inputs option right above
# because we imported 'math' right above python will read inputted program as follow
# will be printed out as: simple interest will be stored as A = P mutiple by "math.pow"(1 plus r),t))
# program will then print out "Simple interest will be R",A where A is the answer store as A


# if 'finance' is equal to 'compound' the following statement will follow for calculation
# r is equal to 'percentage' devided by 100
# P is equal to 'deposit'
# t is equal to 'years'
# above will be substituted in the formula based on the investment inputs option right above
# compound interest will be stored as A = P mutiple (1 plus r mutiple by t)
# program will then print out "Compound interest will be R",A where A is the answer store as A



#******************** bond ********************
    
if (finance == "bond") or (finance == "BOND") or (finance == "Bond"):
    
# if "investment" is not inputted by user based on there format    
# finance is used to store the variable that been inputted by user
# user needs to put in investment or bond
# if bond is inputted then finance is equal to Bond or bond or BOND

    house_value = int(input("What is the present value of the house?: R"))
    interest_rate = int(input("What is the interest rate?: "))
    months = int(input("What is the number of months you plan to take to repay the bond: "))
    
# The same applies as investment above

#*** Bond repayment formula for bond ***

    P = house_value
    i = interest_rate / 12 /100
    n = months
    repayment = (i*P)/(1 -(1+i)**(-n))
    print("The following amount needs to be paid each month: R" + str(repayment))
    
#if finance is equal to simple the following statement will follow for calculation
# P is equal to house_value
# i is equal to interest_rate devided by 12 months (annualy)
# n is equal to months
# above will be substituted in the formula based on the investment inputs option of "***bond***" above
# Bond repayment formula will be stored as repayment equal (i mutiple by P) then devided by (1 plus i) exponet (-n))
# program will then print out "The following amount needs to be paid each month: R" + str(repayment)) str is used to cast integer to a string

else:
    print("Please enter correct wording")
# iF all else fails program will print out ("Please enter correct wording")

