import random_func
import game_func
import time


money = 100
user_class = game_func.UserCtrl(100)
print("\nWelcome to the casino\nYou can play:\ncoin_flip\ncho_han\ncard_game\nroulette\n\nleave\n\nShow(TO SHOW MEUN)")


invalidInput = "Invalid Input (Not enough money || Not a number)"
while True:
    print(f"                             =You have {user_class.money} usd=")
    user = input(">").upper()
    if user == "SHOW":
        print("\nYou can play:\ncoin_flip\ncho_han\ncard_game\nroulette\n\nleave\n\nShow(TO SHOW MEUN)")
    elif user == "LEAVE":
        print("Thanks for visiting the place")
        time.sleep(3)
        break
    elif user == "COIN_FLIP":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, user_class.money)
        if is_bettable == True:
            user_class.money += user_class.coin_flip(int(i))
        else:
            print(invalidInput)
    elif user == "CHO_HAN":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, user_class.money)
        if is_bettable == True:
            user_class.money += user_class.cho_han(int(i))
        else:
            print(invalidInput)
    elif user == "CARD_GAME":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, user_class.money)
        if is_bettable == True:
            user_class.money += user_class.pick_card(int(i))
        else:
            print(invalidInput)
    elif user == "ROULETTE":
        user_class.money += user_class.roulette(user_class.money)
    else:
        print("Unknown input")
