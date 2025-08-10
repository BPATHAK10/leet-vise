import random

class QuestionPicker:
    @staticmethod
    def pick_random(questions):
        if not questions:
            return None
        return random.choice(questions)
