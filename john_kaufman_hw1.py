#This program can be run on the OSU flip servers by entering 'python john_kaufman_hw1.py' (also works with other versions of python)

#John Kaufman CS 362 Winter 2020 HW1: Python Leap Year Calculator (WITHOUT ERROR HANDLING)
#User enters a year, this returns whether the year is a leap year or not

#Leap year rules: divisible by 4, but not by 100, unless also by 400.


#Get user input
year = int(input("Enter a year, and I will determine if it is a leap year: "));


if year%4 == 0:
	if year%100 == 0:
		if year%400 == 0:
			message = "You entered a leap year"; #Divisible by 400
		else:
			message = "You did not enter a leap year"; #Divisible by 100 but not 400
	else:
		message = "You entered a leap year"; #Divisible by 4 but not 100

else:
	message = "You did not enter a leap year"; #Not divisible by 4

print(message); #Output results
