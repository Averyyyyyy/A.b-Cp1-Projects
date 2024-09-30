#graded quiz avery


score = 0


questions = [
   {"questions": "What is 5 + 5?", "answer": "10"},
    {"questions": "What color is the sky?", "answer": "blue"},
     {"questions": "What is the capital of france?", "answer": "paris"},
      {"questions": "How many states are in the U.S?", "answer": "50"},
       {"questions": "Does A come before B?", "answer": "yes"}
]


for q in questions:
   user_answer =
   input(q["question"] + " ")


   if user_answer.lower() == q["answer"].lower():
       score += 1


       print(f"\nYour final score is: {score} out of {len(questions)}")


       if score == len(questions):
           print("Excellent! You answered all questions correctly.")
       elif score >= len(questions) // 2:
           print("Good job! You answered more than half of the questions correctly.")
       else:
           print("Better luck next time!")
