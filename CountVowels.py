#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2

# Function to count vowel ignoring special characters and punctuation.
def vowel_count(word):
	
	# Initializing count variable to 0
	vowel_count = 0
	
	# Creating a set of vowels
	vowels = set("aeiouAEIOU")
	
	# Loop to traverse the alphabet in the given string
	for alphabet in word:
		if alphabet in vowels:
	#If vowel is present it adds to the count.
			vowel_count += 1 
	return vowel_count

#User input for vowel count
word = input("Write words to determine how many vowels are there: ")
print(vowel_count(word))