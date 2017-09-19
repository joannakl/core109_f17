# available_toppings = ['mushrooms', 'olives', 'green peppers',
#         'pepperoni', 'pinapple', 'extra cheese']
#         
# requested_toppings = ['mushrooms', 'sausage', 'Olives']
# 
# for topping in requested_toppings: 
#     if topping in available_toppings :
#         print ('Adding', topping, '.')
#     else:
#         print ("Sorry, we don't have", topping, ".") 
# 
# print("\nFinished making your pizza.\nEnjoy!") 

# This program determines if a customer qulifies for a loan

min_salary = 30000.00
min_years_employed = 2 

# get custormer's salary
salary = float(input("Enter your annual salary: "))
# get the number of years employed
years = int(input("How many years have you been employed: "))

#determine if cusomer qualifies
if salary > min_salary:
    if years > min_years_employed:
        print ('\nYou qualify for the loaa.')
    else:
        print ('\nYou must have been employed for at least', min_years_employed,
           'to qualify.')
else:
    print ('\nYou must earn at leas $', min_salary, ' to qualify.', sep='') 