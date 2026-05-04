def render(board_width,board_height,shots):
    header = "+" + "-"*board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")
        # print("|" + " "*board_width + "|")

    print(header)


if __name__ == "__main__":
    shots = []
    while True:
        inp = input("Where You want to shoot? \n")
        # todo : deal with invalid input
        x,y = inp.split(",")
        x = int(x)
        y = int(y)
        shots.append((x,y))
        render(10,10,shots)

    