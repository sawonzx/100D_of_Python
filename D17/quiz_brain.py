class QuizBrain:

    def __init__(self, qlist):
        self.q_num = 0
        self.q_list = qlist
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.q_list)


    def next_question(self):
        q = self.q_list[self.q_num]
        self.q_num += 1
        user_input = input(f"Q.{self.q_num}: {q.text} (True/False)?: ")
        self.check_answer(user_input, q.answer)
        print("\n")

    def check_answer(self, user_input, answer):
        if user_input == answer:
            self.score += 1
            print("You got it Right!")
        else:
            print("You got it wrong!")
        print(f"The Correct answer was {answer}")
        print(f"Your current score is {self.score}/{self.q_num}")
