#Write a program that accepts a string as input, capitalizes the first letter of each word in the
#string, and then returns the result string.

#Examples:
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming"

#Start of the Code👇👇
# Creates a function that splits the sentence into words
def Capitalize_first_letters(my_text):

# split() method splits the strings
  text = my_text.split()

  #For loop iterates over the list of words
  #capitalize() method capitalizes the first letter of each word
  capitalized_text = [word.capitalize() for word in text]

  #join() method joins the capitalized words
  return " ".join(capitalized_text)

#User inputs a value and an output is produced by invoking the above function
my_text = input("Write a sentence: ")
print(Capitalize_first_letters(my_text))