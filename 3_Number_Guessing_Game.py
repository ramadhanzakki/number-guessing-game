import random

def best_score(attempt):
    best_score_in_game = 0
    if best_score_in_game == 0:
        best_score_in_game += attempt
        return best_score_in_game
    else:
        if best_score_in_game < attempt:
            best_score_in_game == attempt
        else:
            return best_score_in_game

def number_guessing_game():
    while True:
        play_game = input('Play this game?(y/n): ')
        if play_game == "y" or play_game == "Y":
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
                        f"Congratulations!, you guess the number in {attempt} attempt\nYour best score is {best_score(attempt)} attempt")
                    break
                elif user_guess > random_number:
                    print("Too High! Try again")
                elif attempt >= 5:
                    print("Your chance is over. You Lose!")
                    break
                else:
                    print("Too Low! Try again")
        elif play_game == "n" or play_game == "Y":
            break
        else:
            print("Y/N ? ")

if __name__ == "__main__":
    number_guessing_game()