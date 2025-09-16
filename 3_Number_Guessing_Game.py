import random


def number_guessing_game():
    while True:
        try:
            range_number_minimum = int(input('Enter the minimum number: '))
            break
        except ValueError:
            print("Error value! input must number")
            continue
    while True:
        try:
            range_number_maximum = int(input('Enter the maximum number: '))
            break
        except ValueError:
            print("Error value! Input must number")
            continue

    random_number = random.randint(range_number_minimum, range_number_maximum)
    attempt = 0

    while True:

        try:
            user_guess = int(input(f'Guess the number!(between {range_number_minimum} - {range_number_maximum}): '))
            attempt += 1
        except ValueError:
            print("Input must number!")
            continue

        if user_guess == random_number:
            print(
                f"Congratulations!, you guess the number in {attempt} attempt")
            break
        elif user_guess > random_number:
            print("Too High! Try again")
        else:
            print("Too Low! Try again")

if __name__ == "__main__":
    number_guessing_game()