#Palindrome checker

#author: avery

#function to check if a word is a palindrome
def check_palindrome(word):
   #convert the input to lowercase and remove spaces
   cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

#compare the word to its reverse
if cleaned_word == cleaned_word[::-1]:
    print(f'"{word}" is a palindrome. ')
else:
    print(f'"{word}" isn\'t a palindrome.')

#tests words
test_words = ["mom", "a", "dad", "bed", "racecar", "word", "step on no pets", "crab", "borrow or rob", "Yes!", "radar", "tom"]

#run tests
for word in test_words:
   check_palindrome(word)