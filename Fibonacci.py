#Write a program to generate the Fibonacci sequence up to 100.

#Using the Iterative method
# U
def fibonacci_iterative(n):

#Initialize the first variable of the sequence(0 and 1)
  a = 0
  b = 1

#For loop is used to add the previous two variables to form a new variable 
  for fibonacci in range(1, n):
    yield a
    a, b = b, a + b

#Displays the solution
n = 100
print(list(fibonacci_iterative(n)))

