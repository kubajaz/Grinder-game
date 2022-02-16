from classes_grinder import (
    Board,
    Drawer_12,
    Drawer_3,
    Drawer_6,
    Drawer_9,
    Human,
    SmartComputer,
    StupidComputer,
    WrongPawnsNumber,
    WrongGameTribe,
)
from random import choice


def choose_players(board, game_tribe):
    # takes game_tribe and returns two Player instances
    # according to the game tribe
    # choices who starts
    if(game_tribe == "p"):
        player1 = Human(board, "white")
        player2 = Human(board, "black")
    elif(game_tribe == "csm"):
        player1 = choice(["human", "smart_computer"])
        if player1 == "human":
            player1 = Human(board, "white")
            player2 = SmartComputer(board, "black")
        else:
            player1 = SmartComputer(board, "white")
            player2 = Human(board, "black")
    elif(game_tribe == "cst"):
        player1 = choice(["human", "stupid_computer"])
        if player1 == "human":
            player1 = Human(board, "white")
            player2 = StupidComputer(board, "black")
        else:
            player1 = StupidComputer(board, "white")
            player2 = Human(board, "black")
    return player1, player2


def choose_drawer(board):
    # returns drawer depending on pawns number
    if board.pawns() == 3:
        drawer = Drawer_3(board)
    elif board.pawns() == 6:
        drawer = Drawer_6(board)
    elif board.pawns() == 9:
        drawer = Drawer_9(board)
    elif board.pawns() == 12:
        drawer = Drawer_12(board)
    return drawer


def choose_pawns_number():
    # returns pawns number
    while True:
        # loop works until valid input is written
        # else throws errors
        pawns = input('number of pawns: ')
        try:
            if pawns in ['3', '6', '9', '12']:
                pawns = int(pawns)
                break
            else:
                raise WrongPawnsNumber
        except WrongPawnsNumber:
            print("Wrong pawns number! Try again!")
    return pawns


def choose_game_tribe():
    # returns game tribe
    while True:
        # loop works until valid input is written
        # else throws errors
        game_tribe = input('choose game tribe: ')
        try:
            if game_tribe in ['p', 'csm', 'cst']:
                break
            else:
                raise WrongGameTribe
        except WrongGameTribe:
            print("Wrong game tribe! Try again!")
    return game_tribe


def main():
    # user interface
    print("Hello, welcome to our game!")
    print("How many pawns do you want to play?")
    print("Your options are: 3, 6, 9, 12")
    pawns = choose_pawns_number()

    # creates board instance for a game
    board = Board(pawns)
    # creates drawer instance
    drawer = choose_drawer(board)

    print("If you want to play person vs person print 'p'")
    print("If you want to play person vs smart computer print 'csm'")
    print("If you want to play person vs stupid computer print 'cst'")
    game_tribe = choose_game_tribe()

    # chooses players depending on game_tribe
    player1, player2 = choose_players(board, game_tribe)
    print(f"{player1.name()} begins")

    winner = None

    # game loop, game runs until someone has 2 pawns
    while (player1.has_above_two_pawns() and player2.has_above_two_pawns()):
        # game is over if a player cannot move
        if player1.is_blocked():
            print("Player1 is blocked. The winner is player2!")
            winner = "player1"
            break

        # draws a board
        drawer.draw()
        # player1 moves
        player1.move_manager()

        # game is over if a player cannot move
        if player2.is_blocked():
            print("Player1 is blocked. The winner is player2!")
            winner = "player2"
            break
        if not player2.has_above_two_pawns():
            winner = "player1"
            break

        # draws a board
        drawer.draw()
        # player2 moves
        player2.move_manager()

    print("Game over!")

    # winner announcement
    if winner is None:
        if(player1.has_above_two_pawns()):
            print("The winner is player1")
        else:
            print("The winner is player2")
    else:
        print(f"The winner is {winner}")
    drawer.draw()


if __name__ == "__main__":
    main()
