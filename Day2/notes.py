#Data types
#String
print("Hello"[0])

#Integer
print(123 + 345)
print(123_456_789)

#Float
3.1419

#Boolean
True
False

#Check type
num_char = len(input("What is your name? "))
print(type(num_char))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#Code challenge 
two_digit_number = input("Type a two digit number. ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
new_digit = int(first_digit) + int(second_digit)
print("Your new digit number is: " + str(new_digit))

#bmi
weight = float(input("What is your weight? (kg)"))
height = float(input("What is your height? (cm)"))
bmi = weight / (height / 100) ** 2
bmi_as_int = round(bmi, 2)
print("Your BMI is: " + str(bmi_as_int))

#f-strings
score = 15
print(f"Your score is {score}")

#Code challenge 
age = input("What is your current age?\n")
age_as_int = int(age)
age_to_reach = 90
age_difference = age_to_reach - age_as_int
months_left = age_difference * 12
weeks_left = age_difference * 52
days_left = age_difference * 365
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
