#Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz".

#For loop used to make a loop that will repeat till end of the range
for number in range(1, 100):
    
#Multiple conditions give solution between divison of both 3 and 5
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("FizzBuzz")
        
    #Displays the result. 
    print(number)
#End of program