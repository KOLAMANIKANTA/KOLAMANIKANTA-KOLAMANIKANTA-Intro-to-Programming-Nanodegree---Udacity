import time
import random


def print_pause(msg_to_print,seconds):
    print(msg_to_print + '\n')
    time.sleep(seconds)


def introduction(item, badvillan):
    print_pause('You rest for a short while. You have been walking in open balcony.\n',2)
    print_pause("Rumor has it that a " + badvillan + " is somewhere around "
                "here, and has been terrifying the nearby village.\n\n",2)
    print_pause('In front of you is a bungalow.\n',2)
    print_pause('To your right is a dark forest.\n',2)
    print_pause('To your left is a cave.\n',2)
    print_pause('In your hand you hold your trusty (but not very '
                'effective) dagger.\n',2)


def forest(item, badvillan):
    if "magical_sword" in item:
        print_pause('\nYou peer cautiously into the forest.',2)
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty forest"
                    " now.",2)
        print_pause('\nYou walk back to the balcony.\n',2)
    else:
        print_pause('\nYou peer cautiously into the forest.',2)
        print_pause('\nIt turns out to be only a very small forest.',2)
        print_pause('\nYour eye catches a glint of metal behind a '
                    'rock.',2)
        print_pause('\nYou have found the magical Sword of Orcrist!',2)
        print_pause('\nYou discard your silly old dagger and take '
                    'the sword with you.',2)
        print_pause('\nYou walk back out to the balcony.\n',2)
        item.append("magical_sword")
    balcony(item, badvillan)


def bungalow(item, badvillan):
    print_pause('\nYou approach the door of the bungalow.',2)
    print_pause("\nYou are about to knock when the door "
                "opens and out steps a " + badvillan + ".",2)
    print_pause("\nEep! This is the " + badvillan + "'s bungalow!",2)
    print_pause("\nThe " + badvillan + " attacks you!\n",2)
    if 'magical_sword' not in item:
        print_pause('You feel a bit under-prepared for this, '
                    'what with only having a tiny dagger.\n',2)
    while True:
        response = input('Would you like to (1) fight or (2) '
                        'run away?')
        if response == '1' or response == 'one':
            if 'magical_sword' in item:
                print_pause("\nAs the " + badvillan + " moves to attack, "
                            "you unsheath your new sword.",2)
                print_pause('\nThe Sword of Orcrist shines brightly in '
                            'your hand as you brace yourself for the '
                            'attack.',2)
                print_pause("\nBut the  " + badvillan + "takes one look at "
                            "your shiny new toy and runs away!",2)
                print_pause("\nYou have rid the town of the " + badvillan +
                            ". You are victorious!\n",2)
            else:
                print_pause('\nYou do your best...',2)
                print_pause("but your dagger is no match for the "
                            + badvillan + ".",2)
                print_pause('\nYou have been defeated!\n',2)
            play_again()
            break
        if response == '2' or response == 'two':
            print_pause("\nYou run back into the balcony. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n",2)
            balcony(item, badvillan)
            break


def balcony(item, badvillan):
    print_pause('Enter 1 to knock on the door of the bungalow.',2)
    print_pause('Enter 2 to peer into the forest.',2)
    print_pause('What would you like to do?',2)
    while True:
        choice = input('(Please enter 1 or 2.)\n')
        if choice == '1' or choice == 'one':
            bungalow(item, badvillan)
            break
        elif choice == '2' or choice == 'two':
            forest(item, badvillan)
            break
			
def play_again():
    again = input('Would you like to play again? (yes/no)').lower()
    if again == 'y' or again =='yes' or again == 'Y' or again == 'YES':
        print_pause('\n\n\nExcellent! Restarting the game ...\n\n\n',2)
        play_game()
    elif again == 'n' or again == 'no' or again == 'N' or again == 'NO':
        print_pause('\n\n\nThanks for playing! See you next time.\n\n\n',2)
    else:
        play_again()

def play_game():
    item = []
    badvillan = random.choice(['William', 'James', 'Oliver', 'Bunny',
                            'Manikanta','Charan'])
    introduction(item, badvillan)
    balcony(item, badvillan)


play_game()
