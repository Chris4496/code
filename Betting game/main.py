import os
import shelve
import random_func
import game_func
import log_in_func
import time


while True:
    user = input("Create or login account?\n>")
    if user.upper() == "C":
        user_new_name = input("Name:")
        user_new_password = input("Password:")
        name, password, money = log_in_func.creat_acc(
            "betting_game", user_new_name, int(user_new_password), 100)
        user_class = game_func.UserCtrl(money)
        break
    elif user.upper() == "L":
        user_name = input("Please enter your username:")
        user_password = input("Please enter your password:")
        try:
            name, password, money = log_in_func.login_acc(
                "betting_game", user_name, int(user_password))
            user_class = game_func.UserCtrl(money)
            break
        except TypeError:
            pass
    else:
        print("Unknown Input")


print("\nWelcome to the casino\nYou can play:\ncoin_flip\ncho_han\ncard_game\nroulette\n\nleave\n\nShow(TO SHOW MEUN)")

file = shelve.open(name)
invalidInput = "Invalid Input (Not enough money || Not a number)"
while True:
    file['value2'] = user_class.money
    print(f"                             =You have {user_class.money} usd=")
    user = input(">").upper()
    if user == "SHOW":
        print("\nYou can play:\ncoin_flip\ncho_han\ncard_game\nroulette\n\nleave\n\nShow(TO SHOW MEUN)")
    elif user == "LEAVE":
        print("Thanks for visiting the place")
        time.sleep(3)
        file.close
        break
    elif user == "COIN_FLIP":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, name)
        if is_bettable == True:
            user_class.money += user_class.coin_flip(int(i))
        else:
            print(invalidInput)
    elif user == "CHO_HAN":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, name)
        if is_bettable == True:
            user_class.money += user_class.cho_han(int(i))
        else:
            print(invalidInput)
    elif user == "CARD_GAME":
        i = input('How much are u betting:')
        is_bettable = random_func.isbettable(i, name)
        if is_bettable == True:
            user_class.money += user_class.pick_card(int(i))
        else:
            print(invalidInput)
    elif user == "ROULETTE":
        user_class.money += user_class.roulette(user_class.money)
    else:
        print("Unknown input")
