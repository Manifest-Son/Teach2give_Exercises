#Write a program that takes an integer as input and returns true if the input is a power of two.

#Examples:
#8=> returns true
#6=> returns false

#Function creates values that are powers of two.
def power_of_two_loop(number):

#Tests an integer if is a whole number
    if number <= 0:
        return False
    
#while loop tests the value to prove is a power of two
    while number > 1:
        if  number % 2 != 0:
            return False
        number //= 2
    return True

#User inputs a value, the program displays the result
value = int(input("Write a number to determine whether it is a power of two: "))
print(power_of_two_loop(value))
