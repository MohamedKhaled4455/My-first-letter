for row in range(11):
    for col in range(11):
        if col == 0 or col == 10 or ((row == col) and (col > 0 and col < 6)) or (row == 1 and col == 9) or (row == 2 and col == 8) or (row == 3 and col == 7) or (row == 4 and col == 6):
            print("** ", end="")
        else:
            print(end="   ")
    print()
