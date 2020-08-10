import shelve
import os


def creat_acc(dir, title, value1, value2):
    try:
        os.chdir(f"C:\\Users\\Chris\\File for python\\log_in_func_dir\\{dir}")
    except FileNotFoundError:
        raise Exception(f"NoSuchFile no file named {dir}. Make sure you make a folder in *log_in_func_dir*")
    file = shelve.open(title)
    file["value1"] = value1
    file["value2"] = value2
    return title, value1, value2


def login_acc(dir, login_title, value1):
    try:
        os.chdir(f"C:\\Users\\Chris\\File for python\\log_in_func_dir\\{dir}")
    except FileNotFoundError:
        raise Exception("NoSuchFile make sure you make a folder in *log_in_func_dir*")
    have_acc = False
    while True:
        regex_name = f'{login_title}.bak'
        acc_names = os.listdir('.')
        for name in acc_names:
            if regex_name == name:
                have_acc = True
        if have_acc:
            file = shelve.open(login_title)
            while True:
                if value1 == file["value1"]:
                    return login_title, value1, file["value2"]
                else:
                    print('Wrong password, plz try again')
                    file.close()
                    return False
        else:
            print(f"There's no account named {login_title}")
            return False
