import json

history = []

#counter = 0
title = ""
score = ""
menu_choice = 9  # placeholder to initial menu loop

def main():
    global menu_choice
    while menu_choice != 0:
        try:
            menu_choice = int(input(f"{menu()}\nEnter choice: "))
            print("==" * 30)
        except ValueError:
            print("Enter an integer.")
            continue

        while menu_choice == 1 or menu_choice == 2 or menu_choice == 0:
            if menu_choice == 1:
                try:
                    data_loader("history.json")  # reloads history list
                except ValueError:
                    print("** An issue arose during loading... Program continues **")
                his_retriever()  # append new entry
                data_saver("history.json")
            elif menu_choice == 2:
                data_loader("history.json")
                table_creator(history)
            else:
                break
            menu_choice = 9
            break
        else:
            print("** Select a number that is within range **")


def menu():
    return "==" * 30 + "\nKey in 1 to log new paper completion\nKey in 2 to view table of past completion\nKey in 0 to exit "


def data_saver(pFileName):
    with open(pFileName, "w") as file:
        json.dump(history, file, indent=4)

def data_loader(pFileName):
    global history
    try:
        with open(pFileName, "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

def his_retriever():
    global history, counter, title, score
    title = input("Enter the paper you want to keep track of: ")
    score = input(f"Enter the score you achieved in {title}: ")
    if len(history) != 0:
        counter = history[-1]["counter"] + 1
    else:
        counter = 1
    history.append({"counter": counter, "title": title, "score": score})


def table_creator(pHistory):
    print("{:^5} | {:<25} | {:^6}".format("No.", "Title", "Score"))
    print("-"*44)
    if len(history) == 0:
        print("{:^44}".format("No Content"))
    else:
        for i in range(len(pHistory)):
            print("{:^5} | {:<25} | {:^6}".format(pHistory[i]["counter"], pHistory[i]["title"], pHistory[i]["score"]))


if __name__ == '__main__':
    main()
