#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.

#Create a function that reverses the digits
def reverse_integer(num):
 
 # Define a number that is negative and initialize reversed_num to 0
  negative = num < 0
  reversed_num = 0

 # Use a while loop to reverse the digits order 
  while num:

  # Divide to obtain remainder of num then multiply reversed_num by 10 and add them float divide number by 10 to rev_num
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Return reversed_num.
  return -reversed_num if negative else reversed_num

# Asks for users input and gives an output.
num = int(input("Write an number to reverse it: "))
print(reverse_integer(num))

