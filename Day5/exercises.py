# #For loops
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# sum_height = 0
# number_of_students = 0
# for height in student_heights:
#     sum_height += height
#     number_of_students += 1
# avg_student_height = round(sum_height / number_of_students)

# print(avg_student_height)


# #Highest score
# student_scores = input("Input a list of student score ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")


# #Range function
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# #Adding even numbers
# #option 1
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
# #option 2
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)


#FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)