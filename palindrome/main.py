#Palindrome checker


#author: avery


#function to check if a word is a palindrome
def is_palindrome(word):
   #convert the input to lowercase and remove spaces
   cleaned_word = word.lower().replace(" ", " ").replace("!", "")


   #check if the cleaned word is the same forwards and backwards
   return cleaned_word == cleaned_word[::-1]


#lists of test words and phrases
test_words = ["mom", "a", "dad", "bed", "racecar", "word", "step on no pets", "crab", "borrow or rob", "Yes!", "radar", "tom"]

#loop through each test word and check if it's a palindrome
for word in test_words:
   if is_palindrome(word):
       print(f'"{word}" is a palindrome.')
   else:
       print(f'"{word}" is not a palindrome.')