# -*- coding: utf-8 -*-


def spaces(size=1):
    sp = ""
    for i in range(size):
        sp += " "
    return sp


def wave(text, length=170, width=2.5, height=0.3, isCont=True):
    text = (f"{text}")
    space = ""
    sc = 0
    incs = 0
    dir_ = "r"
    max_spaces = 0
    was_inc = False
    for i in range(length):
        if (dir_ == "r"):
            if (incs < width and not was_inc):
                incs += height
            else:
                was_inc = True
                incs -= height

            sc += incs
            print(f"{spaces(int(sc))}{text}")
            space += " "
            if (incs <= 0):
                max_spaces = int(sc)
                # incs = 0
                dir_ = "l"
        else:
            try:
                if (incs < width and was_inc):
                    incs += height
                else:
                    was_inc = False
                    incs -= height
                sc -= (incs)
            except:
                pass
            print(f"{spaces(int(sc))}{text}")
            if (incs < 0):
                sc = 0
                while (incs < 0):
                    incs += height
                dir_ = "r"
        # print(int(sc))
    if (isCont):
        splits(text, 40, int(sc), max_spaces, width, height)


def splits(text, max_lines=40, start_space=0, max_spaces=1, width=1, height=1):
    was_inc = True
    incs = 0
    while (start_space > 0):
        if (incs < width and was_inc):
            incs += height
        else:
            was_inc = False
            incs -= height
        start_space -= (incs)
        print(f"{spaces(int(start_space))}{text}")
    ls_text = list(text)
    text_len = len(text)
    sps = 1
    new_string = text
    total = max_spaces
    n_placed = 0
    isPlaced = False
    last = ""
    des_ = total - 1
    for i in range(len(text)):
        isPlaced = False
        # if(ls_text[len(ls_text)-1-i] != " "):
        while (not isPlaced):
            print(
                f"{text[:-(i+1)]}{spaces(sps)}{ls_text[len(ls_text)-1-i]}{spaces(des_)}{last}"
            )
            sps += 1
            des_ -= 1
            if (sps >= total - n_placed):
                last = f"{ls_text[len(ls_text)-1-i]}{last}"
                isPlaced = True
                sps = 1
                n_placed += 1
                des_ = total - n_placed
    start_space = sps + des_
    incs = 0
    was_inc = True
    while (start_space > 0):
        if (incs < width and was_inc):
            incs += height
        else:
            was_inc = False
            incs -= height
        start_space -= (incs)
        print(f"{spaces(int(start_space))}{text}")
    # wave(text, 100, 2.5, 0.3, False)


def main():
    print("Enter text : ")
    text = str(input())
    print("\n\nUse default or customize?\n\t[1] Default\n\t[2] Customize")
    option = int(input())
    if (option == 2):
        print("\n\nEnter number of lines : ")
        lines = int(input())
        print("\n\nEnter wave width : ")
        width = float(input())
        print("\n\nEnter wave height : ")
        height = float(input())
        print("\n\n")
        wave(text, lines, width, height)
    elif (option == 1):
        wave(text)
    else:
        print("\n\nPlease select a valid option!")
        main()


main()
