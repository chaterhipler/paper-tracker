title_record = []  # storage of the name of different papers, e.g. 2P 2024
score_record = []
counter_record = []

counter = 0
title = ""
score = ""
menu_choice = 9  # any integer other than menu selections / 0

def menu():
    return "\nKey in 1 to log new paper completion\nKey in 2 to view table of past completion\nKey in 0 to exit "

def his_retriever():
    global counter, title, title_record, score_record, score
    title = input("Enter the paper you want to keep track of:")
    title_record.append(title)
    score = input(f"Enter the score you achieved in {title}:")
    score_record.append(score)
    counter += 1
    counter_record.append(counter)


def table_creator(pTitle_rec, pScore_rec, pCounter_rec):
    print("{:^4} | {:<25} | {:^4}".format("No.", "Title", "Score"))
    print("-"*43)
    for i in range(0, len(counter_record)):
        print("{:^4} | {:<25} | {:^4}".format(pCounter_rec[i], pTitle_rec[i], pScore_rec[i]))

# ---------main------------------
while menu_choice != 0:
    try:
        menu_choice = int(input(f"{menu()}\nEnter choice: "))
    except ValueError:
        print("Enter an integer.")

    while menu_choice == 1 or menu_choice == 2:
        if menu_choice == 1:
            his_retriever()
        else:
            table_creator(title_record, score_record, counter_record)
        menu_choice = 9
        break

