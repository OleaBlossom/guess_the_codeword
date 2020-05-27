import os
import random


def intro():
    print('''
                *********************
                *   ROCKET LAUNCH   *
                *********************
                      .
                     .'.
                     |o|  - We're going to the moon!
                    .'o'.         Are you coming?
                    |.-.|
                    '   '
    Guess the secret code word to be allowed on the flight to the moon.
    Input a letter.
    If it appears in the code word, you can keep guessing.
    If not, the rocket will continue staging without you.
    Try not to miss the flight!
    ''')


def choose_word(secret_words):
    random.shuffle(secret_words)
    return secret_words.pop().upper()


def draw_rocket(rocket, guess_count):
    rocket_lines = [str(line) for line in rocket[:guess_count]]
    print('\n'.join(rocket_lines))


def game_over(result, secret_word, rocket):
    os.system('clear')

    if result == "win":
        message = "Hooray! You made it to the moon with the codeword % s" % secret_word
    else:
        message = "You didn't make it to the moon.\n % s was the codeword." % secret_word

    end_text_a = '''

        *******************
        *    GAME OVER    *
        *******************

                             .-.
                            ( (
                             `-'

%s\n
''' % message

    end_text_b = '\n'.join([str(line) for line in rocket])
    end_text_c = '''
                   ( )
                    )
                   ( )

    '''

    print(''.join(end_text_a + end_text_b + end_text_c))


def number_of_rounds(n):
    valid_input = False
    while not valid_input:
        print("Enter the number of rounds you'd like to play, up to %s." %
              n)
        try:
            rounds = int(input("Number of rounds: "))
            if rounds > 0 and rounds < (n + 1):
                valid_input = True
        except:  # check valid input
            print("That is not valid input. Please try again.")

    return rounds


def print_rounds(n):
    if n == 1:
        return "1 round"
    else:
        return "%s rounds" % n


def main():
    secret_words = ["ascension", "aperture", "asteroid", "astronaut", "astronomy", "celestial", "cosmos", "cosmonaut", "comet", "doppler", "eclipse", "equinox", "galaxy", "gravitation", "helium", "hydrogen", "interstellar", "lunar", "light-year", "moon", "meteorite",
                    "nebula", "observatory", "orbit", "parallax", "planet", "radiant", "satellite", "spectrum", "starlight", "solstice", "supernova", "twinkling", "telescope", "universe", "vacuum", "weightlessness", "wormhole", "wavelength", "x-rays", "zenith", "zodiac"]
    number_of_words = len(secret_words)

    rocket = ["                    .",
              "                   .'.",
              "                   |o|",
              "                  .'o'.",
              "                  |.-.|",
              "                  '   '"]
    guess_limit = len(rocket)

    current_round = 1
    win_count = 0
    loss_count = 0
    total_rounds = number_of_rounds(number_of_words)
    rounds_won = print_rounds(win_count)
    rounds_lost = print_rounds(loss_count)

    while current_round <= total_rounds:
        print('''You are playing round %s of %s.
        So far, you have lost %s and won %s.'''
              % (current_round, total_rounds, rounds_lost, rounds_won))

        secret_word = choose_word(secret_words)
        player_guess = ''
        guess_count = 0
        out_of_guesses = False
        guessed_letters = []
        word_guessed = []
        joined_word = ""

        for letter in secret_word:
            if letter.isalpha():
                word_guessed.append("*")
            else:
                word_guessed.append(letter)

        while out_of_guesses is False and "*" in word_guessed:
            attempt_number = guess_limit - guess_count
            if attempt_number == 1:
                print("\nYou have 1 attempt remaining")
            else:
                print("\nYou have %s attempts remaining" % attempt_number)

            joined_word = "".join(word_guessed)
            print("So far, you've correctly guessed: %s" % joined_word)

            try:
                player_guess = str(input("Enter guess: ")).upper()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:   # check there was input, and it is a letter.
                if not player_guess.isalpha():
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1:  # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters:  # check letter hasn't been guessed already
                    print("You have already guessed %s. Please try again." %
                          player_guess)
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(secret_word)):
                if player_guess == secret_word[letter]:
                    # replace all letters in the chosen word that match the players guess
                    word_guessed[letter] = player_guess

            if player_guess not in secret_word:
                guess_count += 1
                draw_rocket(rocket, guess_count)
                if guess_count == guess_limit:
                    out_of_guesses = True

        current_round += 1

        if "*" not in word_guessed:  # no blanks remaining
            game_over("win", secret_word, rocket)
            win_count += 1
            rounds_won = print_rounds(win_count)

        if out_of_guesses:
            game_over("lose", secret_word, rocket)
            loss_count += 1
            rounds_lost = print_rounds(loss_count)

    print('''You played %s rounds.
    You lost %s and won %s.''' % (total_rounds, rounds_lost, rounds_won))


if __name__ == "__main__":
    intro()
    main()
