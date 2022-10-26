MAX_ROUND = 3
P1_SYMBOL = "X"
P2_SYMBOL = "O"
p1_points = 0
p2_points = 0
round_no = 0

def display_initial_game_info():
    print("\n\n\t\t\t\tTIC TAC TOE\n\n")
    print(f"\nSymbol of Player 1: {P1_SYMBOL}")
    print(f"\nSymbol of Player 2: {P2_SYMBOL}")
    print(f"\nround {round_no}")

def show_matrix():
    print("\n\n\n\n")
    print(f"\t\t\t\t {a[0]} | {a[1]} | {a[2]}")
    print("\t\t\t\t---|---|---")
    print(f"\t\t\t\t {a[3]} | {a[4]} | {a[5]}")
    print("\t\t\t\t---|---|---")
    print(f"\t\t\t\t {a[6]} | {a[7]} | {a[8]}")

def start_game():
    global p1_points, p2_points
    for i in range(9):
        if i % 2 == 0:
            choice = int(input(f"\nPlayer 1 Chance({P1_SYMBOL}): "))
            a[choice - 1] = P1_SYMBOL
            result = end()
            if result == P1_SYMBOL:
                print("\n" * 100)
                show_matrix()
                print(f"\n\n\t\t\tPlayer 1 Won the Round {round_no}....!!!!")
                p1_points += 1
                break
            elif result == P2_SYMBOL:
                print("\n" * 100)
                show_matrix()
                print(f"\n\n\t\t\tPlayer 2 Won the Round {round_no}....!!!!")
                p2_points += 1
                break
            print("\n" * 100)
            show_matrix()
        else:
            choice = int(input(f"\nPlayer 2 Chance({P2_SYMBOL}): "))
            a[choice - 1] = P2_SYMBOL
            result = end()
            if result == P1_SYMBOL:
                print("\n" * 100)
                show_matrix()
                print(f"\n\n\t\t\tPlayer 1 Won the Round {round_no}....!!!!")
                p1_points += 1
                break
            elif result == P2_SYMBOL:
                print("\n" * 100)
                show_matrix()
                print(f"\n\n\t\t\tPlayer 2 Won the Round {round_no}....!!!!")
                p2_points += 1
                break
            print("\n" * 100)
            show_matrix()
    result = end()
    if result == "no_winner":
        print("\n\n\t\t\tGame is Drawn....!!!!")

def end():
	if( (a[0] == a[1] == a[2] == P1_SYMBOL) or (a[3] == a[4] == a[5] == P1_SYMBOL) or (a[6] == a[7] == a[8] == P1_SYMBOL) ):
		return P1_SYMBOL
	elif( (a[0] == a[1] == a[2] == P2_SYMBOL) or (a[3] == a[4] == a[5] == P2_SYMBOL) or (a[6] == a[7] == a[8] == P2_SYMBOL) ): 
		return P2_SYMBOL
	elif( (a[0] == a[3] == a[6] == P1_SYMBOL) or (a[1] == a[4] == a[7] == P1_SYMBOL) or (a[2] == a[5] == a[8] == P1_SYMBOL) ):
		return P1_SYMBOL
	elif( (a[0] == a[3] == a[6] == P2_SYMBOL) or (a[1] == a[4] == a[7] == P2_SYMBOL) or (a[2] == a[5] == a[8] == P2_SYMBOL) ):
		return P2_SYMBOL
	elif( (a[0] == a[4] == a[8] == P1_SYMBOL) or (a[2] == a[4] == a[6] == P1_SYMBOL) ):
		return P1_SYMBOL
	elif( (a[0] == a[4] == a[8] == P2_SYMBOL) or (a[2] == a[4] == a[6] == P2_SYMBOL) ):
		return P2_SYMBOL
	else:
		return "no_winner"

def show_winner_of_game():
    print("\n" * 100)
    print(f"\n\t\t\tPoints of Player 1:- {p1_points}")
    print(f"\n\t\t\tPoints of Player 2:- {p2_points}")
    if p1_points > p2_points:
        print("\n\n\n\n\t\t!!!!....Player 1 Won the Game....!!!!")
    elif p1_points < p2_points:
        print("\n\n\n\n\t\t!!!!....Player 2 Won the Game....!!!!")
    elif p1_points == p2_points:
        print("\n\n\n\n\t\t!!!!....Game is Drawn....!!!!")


while round_no < MAX_ROUND:
    round_no += 1
    print("\n" * 100)
    display_initial_game_info()
    a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    show_matrix()
    start_game()
    if round_no < MAX_ROUND:
        input("\n\n\n\n\n\n\n\n\nPress Enter To Start The Next Round....")
    else:
        input("\n\n\n\n\n\n\n\n\nPress Enter To See The Results....")
show_winner_of_game()