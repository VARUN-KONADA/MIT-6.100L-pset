## 6.100A PSet 1: Part A
## Name:varun
## Time Spent:
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary =  float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
cost_of_dream_home = float(input("Enter the cost of your dream home: ")) 

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25                         #25%
cost_of_downpayment = cost_of_dream_home * portion_down_payment
amount_saved = 0                                    # initial savings
monthly_salary = yearly_salary / 12  
monthly_savings = monthly_salary * portion_saved
r = 0.05                                             #annual return
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below #################################################################################################

#savings must be equal or greater than cost of dream home 
while (amount_saved < cost_of_downpayment):
        
    months += 1 
    amount_saved += amount_saved  * (r/12)
    amount_saved += monthly_savings

print("number of month: ", months)





