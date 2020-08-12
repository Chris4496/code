import random
import re


class UserCtrl:
    def __init__(self, money):
        self.money = money

    def coin_flip(self, money):
        print(f'---You bet {money} usd---')
        result = random.choice(["Heads", "Tails"]).upper()
        while True:
            user = input('Heads or Tails:').upper()
            if user == "HEADS" or user == "TAILS":
                print(f"---The result is {result}---")
                m_change = money / 4
                if user == result:
                    print(f'*You won {m_change} usd*')
                    return m_change
                else:
                    print(f'*You lost {m_change} usd*')
                    return -m_change
            else:
                print('invalid input')

    def cho_han(self, money):
        print(f'---You bet {money} usd---')
        sum = random.randint(1, 6) + random.randint(1, 6)
        if (sum % 2) == 0:
            result = "EVEN"
        else:
            result = "ODD"
        while True:
            user = input('Odd or Even:').upper()
            if user == "ODD" or user == "EVEN":
                print(f"---The sum of two dices is {result}({sum})---")
                m_change = money / 2
                if user == result:
                    print(f'*You won {m_change} usd*')
                    return m_change
                else:
                    print(f'*You lost {m_change} usd*')
                    return -m_change
            else:
                print('invalid input')

    def pick_card(self, money):
        card_liba = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "JACK",
            12: "QUEEN",
            13: "KING"
        }
        print(f'---You bet {money} usd---')
        bot = random.randint(1, 13)
        user = random.randint(1, 13)
        display = card_liba.get(user)
        print(f"---You picked {display}---")
        input("press enter to review opponent's card")
        display = card_liba.get(bot)
        print(f"---Your opponent picked a {display}---")
        m_change = money * 0.4
        if user > bot:
            print(f'*You won {m_change} usd*')
            return m_change
        if user < bot:
            print(f'*You lost {m_change} usd*')
            return -m_change
        else:
            print("It's a tie")
            return 0

    def roulette(self, money):
        spots_list = []
        spots_laba = {       # can use range() function
            "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
            "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
            "odd": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35],
            "even": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
            "0": [0],
            "1-12": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],   # Eg. --range(1, 13)--
            "13-24": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            "25-36": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        }
        pay_liba = {
            "red": 1,
            "black": 1,
            "odd": 1,
            "even": 1,
            "0": 40,
            "1-12": 2,
            "13-24": 2,
            "25-36": 2
        }
        print('''Spots to bet in:\n
        \\\\ odd(1/1)              //
        // even(1/1)             \\\\
        \\\\ 0(1/40)               //
        // specific number(1/35) \\\\
        \\\\ red(1/1)              //
        // black(1/1)            \\\\
        \\\\ 1-12(1/2)             //
        // 13-24(1/2)            \\\\
        \\\\ 25-36(1/2)            //
        ''')
        while True:
            print("What spots do you want to bet on? *TYPE DONE IF FINISH*")
            user = input(">")
            if user.upper() == "DONE":
                break
            while True:
                amount = input("How many you want to bet on this spot:")
                if int(amount) > money:
                    print("not enough money")
                else:
                    money -= int(amount)
                    break
            mo = re.search('odd|even|0|red|black|1-12|13-24|25-36|1[0-9]|2[0-9]|3[0-6]|[1-9]', user)
            if mo == None:
                print("unknown spot")
                pass
            elif str(mo.group(0)) != str(user):
                print("unknown spot")
                pass
            else:
                spots_list.append((mo.group(0), amount))
            if money == 0:
                print("You don't have any money left")
                break
            print(spots_list)
        result = random.randint(0, 36)
        # print(result)
        input("press enter to review the result")
        print(f"The result is ---{result}---")
        total_bet_amount = 0
        return_amount = 0
        for spot in spots_list:
            bet_amuont = int(spot[1])
            if spot[0].isdigit():
                spot_list = [int(spot[0])]
            else:
                spot_list = spots_laba.get(spot[0])
            # print(spot_list)
            for i in spot_list:
                if i == result:
                    return_amount += pay_liba.get(spot[0], 35) * bet_amuont
            total_bet_amount += int(spot[1])
        print(f'You bet {total_bet_amount}\n*You won {return_amount}*')
        return return_amount - total_bet_amount

