#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
print(type(total_bill))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
final_amount = ((total_bill + (total_bill * tip_percentage / 100))) / total_people
# print(f"Each person should pay: ${round(final_amount, 2)}")
#tried to round the decimals but to always get a second decimal, used the below code👇
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")
#there are so many ways to calculate but this one just popped in my head first😁