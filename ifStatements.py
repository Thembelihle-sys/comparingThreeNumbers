num1= int(input('Enter first number'))
num2= int(input('Enter second number'))
num3= int(input('Enter third number'))

largest_num = num1
#check if the second number is larger than the current largest number
#update the largest number if needed
if num2 > largest_num:
 largest_num = num2

if num3 > largest_num:
 largest_num = num3

print("The largest number is: ", largest_num)