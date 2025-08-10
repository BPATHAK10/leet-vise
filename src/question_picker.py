import random
from src.config import ONLY_BLIND_75
from src.notion_importer import Question

class QuestionPicker:
    @staticmethod
    def pick_question(questions: list) -> Question | None:
        if not questions:
            return None
        
        # Pick from blind 75 questions
        if ONLY_BLIND_75:
            print("Picking from Blind 75 questions...")
            blind_75_questions = [q for q in questions if q["blind_75"]]
            if blind_75_questions:
                return random.choice(blind_75_questions)
            else:
                print("No Blind 75 questions available. Picking from all questions.")

        return random.choice(questions)
    