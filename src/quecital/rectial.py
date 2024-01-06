import tomllib
from colorama import Fore, Style
from quecital.quecital import find_quecital_toml

def display_prompt(prompt):
    print(f"Prompt: {prompt}")

# Function to compare user input with the recital and provide feedback
def compare_input(user_input, recital):
    # Split the user input and recital into lists of words
    user_words = user_input.split()
    recital_words = recital.split()

    # Initialize counters for correct positions, incorrect positions, and correct characters
    correct_positions = 0
    incorrect_positions = 0
    correct_characters = 0

    # Iterate over the words in user input and recital
    for user_word, recital_word in zip(user_words, recital_words):
        # Calculate the number of correct positions in each word
        correct_positions += sum(user_word[i] == recital_word[i] for i in range(min(len(user_word), len(recital_word))))
        # Calculate the number of incorrect positions in each word
        incorrect_positions += sum(user_word.count(char) for char in recital_word) - correct_positions
        # Calculate the number of correct characters in incorrect positions in each word
        correct_characters += correct_positions - incorrect_positions

    return correct_positions, incorrect_positions, correct_characters

def display_feedback(user_input, recital):
    correct_positions, incorrect_positions, correct_characters = compare_input(user_input, recital)

    for i in range(len(user_input)):
        if user_input[i] == recital[i]:
            print(Fore.GREEN + user_input[i], end=' ')
        elif user_input[i] in recital:
            print(Fore.YELLOW + user_input[i], end=' ')
        else:
            print(Fore.RED + user_input[i], end=' ')

    print(Style.RESET_ALL)
    print(f"Correct Positions: {correct_positions}")
    print(f"Incorrect Positions: {incorrect_positions}")
    print(f"Correct Characters in Incorrect Positions: {correct_characters}")

def main():
    # Read data from quecital.toml
    with open('quecital.toml', 'r') as file:
        data = tomllib.load(file)

    topic = data.get('topic', {})
    recitals = topic.get('recitals', [])

    for recital_data in recitals:
        prompt = recital_data.get('prompt', '')
        recital = recital_data.get('recital', '')

        display_prompt(prompt)

        user_input = input("Your guess: ")

        display_feedback(user_input, recital)

if __name__ == "__main__":
    main()
