import random
import sys
from data import data



# game function
def game():
    print("Game Start!\n")

    vs = """
    _    __
    | |  / /____
    | | / / ___/
    | |/ (__  )
    |___/____(_)
    """

    # pull from the "data" dictionary person A
    person_A = random.choice(data) # pull random dictionary entry
    name_A = person_A["name"] # pull name value from key "name"
    count_A = person_A["follower_count"] # pull count value from key "count"
    desc_A = person_A["description"] # pull description value from key "description"
    country_A = person_A["country"] # pull country value from key "country"
    
    # print person A info
    option_A = print(f"{name_A} is a {desc_A} from {country_A}.") # print name, description, and country

    print(vs)

    keep_playing = True
    while keep_playing = True:
        # pull from "data" dictionary person B
        person_B = random.choice(data) # pull random dictionary entry
        name_B = person_B["name"] # pull name value from key "name"
        count_B = person_B["follower_count"] # pull count value from key "count"
        desc_B = person_B["description"] # pull description value from key "description"
        country_B = person_B["country"] # pull country value from key "country"

        # print person B info
        option_B = print(f"{name_B} is a {desc_B} from {country_B}.\n") # print name, description, and country

        # take guess
        guess = input(f"Is {name_A} total user count '{count_A}' higher than {name_B} subscriber count? (y)es or (n)o: ").lower()
        
        # compare answer
        if count_A > count_B:
            if guess == 'yes' or guess == 'y':
                correct = 'yes'
                return correct
            elif guess == 'no' or guess == 'n':
                print("You guessed incorrectly! GAME OVER!")
                sys.exit()
            else:
                print("Game exit; incorrect selection.")
                main()

        else:
            if guess == 'no' or guess == 'n':
                correct = 'yes'
                return correct
            elif guess == 'yes' or guess == 'y':
                print("You guessed incorrectly! GAME OVER!")
                sys.exit()
            else:
                print("Game exit; incorrect selection.")
                main()

        # if correct, continue 
        play_again = input("Keep playing? (y)es or (n)o: ").lower()
        if play_again == 'yes':
            keep_playing = True
        elif play_again == 'no':
            print("Game over!")
            keep_playing = False
            sys.exit()
        else:
            print("Incorrect selection; game exit...")
            main()



# main function
def main():
    
    logo = """
        __  ___       __
       / / / (_)___ _/ /_  ___  _____
      / /_/ / / __ `/ __ \/ _ \/ ___/
     / __  / / /_/ / / / /  __/ /
    /_/ ///_/\__, /_/ /_/\___/_/
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /
    /_____/\____/|__/|__/\___/_/
    """
    print(logo)

    print("Welcome to Higher-lower game. By XxTheSunxX.")

    while True:
        choice = input("Do you want to play the Higher-Lower Game? (Y)es or (N)o: ").lower()

        if choice == "y" or choice == "yes":
            game()

        elif choice == "n" or choice == "no":
            print("Exiting game...")
            sys.exit()

        else:
            print("Choose either (Y)es or (N)o: ")



if __name__== "__main__":
    main()