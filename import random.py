import random
import time

wallet = 100

def play_bet(wallet):
    if wallet == 0:
        print("Sorry, your wallet is empty. You cannot place any more bets.")
        return wallet

    bet_amount = int(input("Enter the bet amount: "))
    if bet_amount > wallet:
        print("Sorry, you cannot bet more than what you have in your wallet.")
        return wallet

    print("Choose your betting option:")
    print("1. Bet on a specific number")
    print("2. Bet on red")
    print("3. Bet on black")
    print("4. Bet on green")

    option = int(input("Enter the option number (1, 2, 3 or 4): "))

    if option == 1:
        roulette_number = int(input("What number would you like to bet on? 0-36?: "))
        print("Rolling.")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling...")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling.")
        time.sleep(0.6)
        number_rolled = random.randint(0, 36)
        print("The number is:", number_rolled)

        if roulette_number == number_rolled:
            money_won = bet_amount * 36
            time.sleep(1)
            print(f"Congratulations! You won ${money_won}.")
            wallet += money_won
        else:
            time.sleep(1)
            print("Sorry, you lost!")
            wallet -= bet_amount

    elif option == 2:
        print("Rolling.")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling...")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling.")
        time.sleep(0.6)
        color_rolled = random.choices(['red', 'black', 'green'], weights=[18, 18, 1], k=1)[0]
        print("The color is:", color_rolled)

        if color_rolled == 'red':
            money_won = bet_amount * 2
            time.sleep(1)
            print(f"Congratulations! You won ${money_won}.")
            wallet += money_won
        else:
            time.sleep(1)
            print("Sorry, you lost!")
            wallet -= bet_amount

    elif option == 3:
        print("Rolling.")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling...")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling.")
        time.sleep(0.6)
        color_rolled = random.choices(['red', 'black', 'green'], weights=[18, 18, 1], k=1)[0]
        print("The color is:", color_rolled)

        if color_rolled == 'black':
            money_won = bet_amount * 2
            time.sleep(1)
            print(f"Congratulations! You won ${money_won}.")
            wallet += money_won
        else:
            time.sleep(1)
            print("Sorry, you lost!")
            wallet -= bet_amount
    elif option == 4:
        print("Rolling.")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling...")
        time.sleep(0.6)
        print("Rolling..")
        time.sleep(0.6)
        print("Rolling.")
        time.sleep(0.6)
        color_rolled = random.choices(['red', 'black', 'green'], weights=[18, 18, 1], k=1)[0]
        print("The color is:", color_rolled)

        if color_rolled == 'green':
            money_won = bet_amount * 36
            time.sleep(1)
            print(f"Congratulations! You won ${money_won}.")
            wallet += money_won
        else:
            time.sleep(1)
            print("Sorry, you lost!")
            wallet -= bet_amount
    
    else:
        time.sleep(1)
        print("Invalid option. Please enter 1, 2, or 3.")
        return wallet

    time.sleep(1)
    print(f"You have ${wallet} in your wallet.")
    return wallet

print("You have $100 in your wallet.")
while True:
    time.sleep(1)
    print("Would you like to place a bet?")
    user_input = input("Yes or No:").lower()

    if user_input == "no":
        time.sleep(1)
        print("Come again soon!")
        break

    elif user_input == "yes":
        wallet = play_bet(wallet)

    else:
        time.sleep(1)
        print("Invalid input. Please enter 'yes' or 'no'.")
