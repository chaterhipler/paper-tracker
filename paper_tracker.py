history = []

counter = 0
title = ""
score = ""
menu_choice = 9  # placeholder to initial menu loop

def menu():
    return "==" * 30 + "\nKey in 1 to log new paper completion\nKey in 2 to view table of past completion\nKey in 0 to exit "

def his_retriever():
    global history, counter, title, title_record, score_record, score
    title = input("Enter the paper you want to keep track of:")
    score = input(f"Enter the score you achieved in {title}:")
    counter += 1
    history.append({"counter": counter, "title": title, "score": score})
    

def table_creator(pHistory):
    print("{:^5} | {:<25} | {:^6}".format("No.", "Title", "Score"))
    print("-"*44)
    if counter == 0:
        print("{:^44}".format("No Content"))
    else:
        for i in range(len(pHistory)):
            print("{:^5} | {:<25} | {:^6}".format(pHistory[i]["counter"], pHistory[i]["title"], pHistory[i]["score"]))

# ---------------main------------------
while menu_choice != 0:
    try:
        menu_choice = int(input(f"{menu()}\nEnter choice: "))
        print("==" * 30)
    except ValueError:
        print("Enter an integer.")

    while menu_choice == 1 or menu_choice == 2 or menu_choice == 0:
        if menu_choice == 1:
            his_retriever()
        elif menu_choice == 2:
            table_creator(history)
        else:
            break
        menu_choice = 9
        break
    else:
        print("** Select a number that is within range **")

