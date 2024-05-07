import random

def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            return answer
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(quiz_data):
    score = 0

    for category, questions in quiz_data.items():
        print(f"\nCategory: {category}")
        for question, choices, correct_answer in questions:
            display_question(question, choices)
            user_answer = get_user_answer()

            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}: {choices[correct_answer-1]}\n")

    print(f"Quiz complete! Your score: {score} out of {sum(len(questions) for questions in quiz_data.values())}")

def main():
    quiz_data = {
        "General Knowledge": [
            ("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
            ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
            
        ],
        "Science": [
            ("What is the chemical symbol for water?", ["H2O", "CO2", "O2", "N2"], 1),
            ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1),
            
        ],
        "Games":[
          ("Which is the biggest cricket ground in the world?", ["Narendra Modi Stadium", "Wankhede Stadium", "The Oval", "Sydney Cricket Ground"], 1),
          ("Who is the fastest Runner of the world", ["Usen Bolt", "Milkha"],1),
        ]
    }

    random.shuffle(quiz_data["General Knowledge"])  # Shuffle questions in a category for variety
    random.shuffle(quiz_data["Science"])
    random.shuffle(quiz_data["Games"])

    print("Welcome to the Quiz!\nTest your knowledge in various categories.")
    run_quiz(quiz_data)

if __name__ == "__main__":
    main()
