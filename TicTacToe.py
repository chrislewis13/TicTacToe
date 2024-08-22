def Printboard(Xstate, Zstate):
    zero = 'X' if Xstate[0] else ('O' if Zstate[0] else 0) # Place X on O if it is true(Empty) dose same with the O
    one = 'X' if Xstate[1] else ('O' if Zstate[1] else 1)
    two = 'X' if Xstate[2] else ('O' if Zstate[2] else 2)
    three = 'X' if Xstate[3] else ('O' if Zstate[3] else 3)
    four = 'X' if Xstate[4] else ('O' if Zstate[4] else 4)
    five = 'X' if Xstate[5] else ('O' if Zstate[5] else 5)
    six = 'X' if Xstate[6] else ('O' if Zstate[6] else 6)
    seven = 'X' if Xstate[7] else ('O' if Zstate[7] else 7)
    eight = 'X' if Xstate[8] else ('O' if Zstate[8] else 8)
    #Print the actual board
    print(f"|  {zero}    |     {one}    |     {two}  |")
    print("|-------|----------|--------|")
    print(f"|  {three}    |     {four}    |     {five}  |")
    print("|-------|----------|--------|")
    print(f"|  {six}    |     {seven}    |     {eight}  |")


def checkwinner(Xstate, Zstate):    
    winner_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],   
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

    for win in winner_conditions:
        if Xstate[win[0]] + Xstate[win[1]] + Xstate[win[2]] == 3:
            print("X won the match")
            return 1
        if Zstate[win[0]] + Zstate[win[1]] + Zstate[win[2]] == 3:
            print("O won the match")
            return 0
    return -1

#List initilized with 0 as empty list
Xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#1 for x turn and 0 for O turn
turn = 1


#while loop with true to make it infinite
while (True):
    Printboard(Xstate, Zstate)
    if (turn == 1):
        print("X move")
        inp = int(input("Enter a Number between 0 to 8"))
        Xstate[inp] = 1
        

    else:
        print("O move")
        inp = int(input("Enter a Number between 0 to 8"))
        Zstate[inp] = 1
    


    checkwin = checkwinner(Xstate, Zstate)
    if (checkwin != -1):
        print("Match Over")
        break


    turn = 1 - turn # for O turn because 1-1 is 0 which is false
