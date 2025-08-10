import sys
import time
import argparse
from src.config import TIMER_MINUTES
from src.notion_importer import NotionImporter
from src.cache_manager import CacheManager
from src.question_picker import QuestionPicker
from src.display import Display
from src.timer import TimerThread

def main():
    # Handle the arguments
    parser = argparse.ArgumentParser(description="Leet-Vise: LeetCode revision CLI tool")
    parser.add_argument("--import-data", action="store_true", help="Fetch fresh data from Notion API")
    args = parser.parse_args()

    # Initialize cache manager
    cache_manager = CacheManager()

    # Import data if argument is provided
    if args.import_data:
        print("📥 Fetching data from Notion API...")
        importer = NotionImporter()
        data = importer.fetch_from_api()
        cache_manager.save_cache(data)
        print(f"✅ Cache updated with {len(data)} questions.")

    # Load questions from cache
    questions = cache_manager.load_cache()
    if not questions:
        print("No questions found in cache. Run with --import-data to fetch from Notion.")
        sys.exit(1)

    # Welcome display
    Display.welcome()
    input()

    timer_length_sec = TIMER_MINUTES * 60

    while True:
        # Pick a question
        question = QuestionPicker.pick_question(questions)
        if question is None:
            print("No questions available.")
            break
        
        # Show question and start timer
        Display.show_question(question)
        timer = TimerThread(timer_length_sec)
        timer.start()

        start_time = time.time()

        while timer.time_left > 0:
            # Wait for user command
            cmd = input().strip().lower()

            # Handle commands
            if cmd == "h":
                Display.show_hint(question.get("hint", ""))
            elif cmd == "s":
                Display.show_solution(question.get("solution", ""))
            elif cmd == "e":
                timer.stop()
                print("Ending current question early.")
                break
            elif cmd == "q":
                timer.stop()
                print("Goodbye! Happy coding!")
                sys.exit(0)
            else:
                print("Unknown command. Use h, s, e, or q.")

        end_time = time.time()
        time_taken = int(end_time - start_time)

        # See if user solved the question
        solved = input("Did you solve it? (y/n): ").strip().lower() == "y"
        
        if solved:
            print("🎉 Great job on solving the question!")
            print(f"You solved it in: {time_taken} seconds")
        else:
            print("No worries! Keep practicing and you'll get there.")

        # Ask to continue or quit
        cont = input("Press ENTER for next question or type q to quit: ").strip().lower()
        if cont == "q":
            print("Great work today! See you next time.")
            break

if __name__ == "__main__":
    main()
