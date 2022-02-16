from dictionaries import (
    three_pawns_neighbours,
    six_pawns_neighbours,
    nine_pawns_neighbours,
    twelve_pawns_neighbours,
    three_pawns_trios,
    six_pawns_trios,
    nine_pawns_trios,
    twelve_pawns_trios
)

from random import choice


class WrongStateError(ValueError):
    pass


class WrongPawnsNumber(ValueError):
    pass


class WrongPointNumber(IndexError):
    pass


class WrongColorError(ValueError):
    pass


class WrongGameTribe(ValueError):
    pass


class WrongPointError(ValueError):
    pass


class Point():
    def __init__(self, board, id, state="empty", neighbours=None):
        # Takes parameters:
        # board: an instance of class board for this particular game
        # id: number of point (from 0 to list_of_points length-1)
        # state: can be empty, black or white according to the pawn
        # neighbours: list of neighbours of the point
        # the point takes info about number of pawns and trios from the board

        self._pawns = board.pawns()
        self._board = board
        self._id = id
        if (state in ["empty", "black", "white"]):
            self._state = state
        else:
            raise WrongStateError

        if(neighbours is None):
            self._neighbours = []
        else:
            self._neighbours = neighbours
        self._trios = board.trios()[id]

    def pawns(self):
        # returns number of pawns on the board
        return self._pawns

    def board(self):
        # returns an instance of class board
        return self._board

    def id(self):
        # returns id of the point
        return self._id

    def state(self):
        # returns state of the point
        return self._state

    def neighbours(self):
        # returns list of neighbours of the point
        return self._neighbours

    def same_color_neighbours(self):
        # returns list of neighbours which have the same color(state) as point
        neighbours = 0
        if self.state() != "empty":
            for neighbour in self.neighbours():
                point = self.board().list_of_points()[neighbour]
                if point.state() == self.state():
                    neighbours += 1
        return neighbours

    def trios(self):
        # returns list of trios in which the point participates
        # they are taken from dictionaries.py file
        return self._trios

    def set_state(self, new_state):
        # sets the state of the point (black, white, or empty)
        self._state = new_state

    def if_trio(self):
        # checks if point is in trio of three same-color points
        for list in self.trios():
            state1 = self.board().list_of_points()[list[0]].state()
            state2 = self.board().list_of_points()[list[1]].state()
            state3 = self.board().list_of_points()[list[2]].state()
            if(state1 == state2 == state3 == "black"):
                return True
            elif(state1 == state2 == state3 == "white"):
                return True
            continue
        return False

    def whose_pawn(self):
        # returns the number of player which putted a pawn on the point
        # returns 0, when point is empty
        if self.state() == "empty":
            return 0
        elif self.state() == "white":
            return 1
        elif self.state() == "black":
            return 2


class Board():
    def __init__(self, pawns):
        # Takes parameter: pawns
        # Based on pawns number it makes a list of point instances
        if pawns in [3, 6, 9, 12]:
            self._pawns = pawns
        else:
            raise WrongPawnsNumber
        if pawns == 3:
            self._trios = three_pawns_trios
            list_of_points = []
            for i in range(9):
                point = Point(self, i, "empty", three_pawns_neighbours[i])
                list_of_points.append(point)
            self._list_of_points = list_of_points
        elif pawns == 6:
            self._trios = six_pawns_trios
            list_of_points = []
            for i in range(16):
                point = Point(self, i, "empty", six_pawns_neighbours[i])
                list_of_points.append(point)
            self._list_of_points = list_of_points
        elif pawns == 9:
            self._trios = nine_pawns_trios
            list_of_points = []
            for i in range(24):
                point = Point(self, i, "empty", nine_pawns_neighbours[i])
                list_of_points.append(point)
            self._list_of_points = list_of_points
        elif pawns == 12:
            self._trios = twelve_pawns_trios
            list_of_points = []
            for i in range(24):
                point = Point(self, i, "empty", twelve_pawns_neighbours[i])
                list_of_points.append(point)
            self._list_of_points = list_of_points

    def pawns(self):
        # returns number of pawns
        return self._pawns

    def trios(self):
        # returns list of all trios on the board
        # every trio is a single list of point ids
        return self._trios

    def list_of_points(self):
        # returns list of points, which is a representation of the board
        return self._list_of_points


class Drawer():
    def __init__(self, board):
        self.board = board


class Drawer_3(Drawer):
    def __init__(self, board):
        super().__init__(board)

    def draw(self):
        # draws a board with 3 pawns in terminal
        list = []
        for point in self.board.list_of_points():
            index = point.whose_pawn()
            list.append(index)
        print(f"\n{list[0]}-{list[1]}-{list[2]}")
        print("|\|/|")
        print(f"{list[3]}-{list[4]}-{list[5]}")
        print("|/|\|")
        print(f"{list[6]}-{list[7]}-{list[8]}\n")


class Drawer_6(Drawer):
    def __init__(self, board):
        super().__init__(board)

    def draw(self):
        # draws a board with 6 pawns in terminal
        list = []
        for point in self.board.list_of_points():
            index = point.whose_pawn()
            list.append(index)
        print(f"\n{list[0]}---{list[1]}---{list[2]}")
        print("|   |   |")
        print(f"| {list[3]}-{list[4]}-{list[5]} |")
        print("| |   | |")
        print(f"{list[6]}-{list[7]}   {list[8]}-{list[9]}")
        print("| |   | |")
        print(f"| {list[10]}-{list[11]}-{list[12]} |")
        print("|   |   |")
        print(f"{list[13]}---{list[14]}---{list[15]}\n")


class Drawer_9(Drawer):
    def __init__(self, board):
        super().__init__(board)

    def draw(self):
        # draws a board with 9 pawns in terminal
        list = []
        for point in self.board.list_of_points():
            index = point.whose_pawn()
            list.append(index)
        print(f"\n{list[0]}-----{list[1]}-----{list[2]}")
        print("|     |     |")
        print(f"| {list[3]}---{list[4]}---{list[5]} |")
        print("| |   |   | |")
        print(f"| | {list[6]}-{list[7]}-{list[8]} | |")
        print("| | |   | | |")
        part1 = f"{list[9]}-{list[10]}-{list[11]}   {list[12]}"
        part2 = f"-{list[13]}-{list[14]}"
        print(part1 + part2)
        print("| | |   | | |")
        print(f"| | {list[15]}-{list[16]}-{list[17]} | |")
        print("| |   |   | |")
        print(f"| {list[18]}---{list[19]}---{list[20]} |")
        print("|     |     |")
        print(f"{list[21]}-----{list[22]}-----{list[23]}\n")


class Drawer_12(Drawer):
    def __init__(self, board):
        super().__init__(board)

    def draw(self):
        # draws a board with 12 pawns in terminal
        list = []
        for point in self.board.list_of_points():
            index = point.whose_pawn()
            list.append(index)
        print(f"\n{list[0]}-----{list[1]}-----{list[2]}")
        print("|\    |    /|")
        print(f"| {list[3]}---{list[4]}---{list[5]} |")
        print("| |\  |  /| |")
        print(f"| | {list[6]}-{list[7]}-{list[8]} | |")
        print("| | |   | | |")
        part1 = f"{list[9]}-{list[10]}-{list[11]}   {list[12]}"
        part2 = f"-{list[13]}-{list[14]}"
        print(part1 + part2)
        print("| | |   | | |")
        print(f"| | {list[15]}-{list[16]}-{list[17]} | |")
        print("| |/  |  \| |")
        print(f"| {list[18]}---{list[19]}---{list[20]} |")
        print("|/    |    \|")
        print(f"{list[21]}-----{list[22]}-----{list[23]}\n")


class Player():
    def __init__(self, board, color):
        # Takes parameters:
        # board: an instance of class board for this game
        # color: white or black
        # from board it takes number of pawns, list of points

        self._pawns = board.pawns()
        if color in ["black", "white"]:
            self._color = color
        else:
            raise WrongColorError
        self._opp_color = "black" if color == "white" else "white"
        self._board = board
        self._unused_pawns = self._pawns

    def unused_pawns(self):
        # returns number of pawns not used yet
        # in the beginning it equals the number of all pawns
        # it decreases while pawn are being putted on the board
        return self._unused_pawns

    def playing_pawns(self):
        # returns number of playing(laying on the board) pawns
        playing_pawns = 0
        for point in self.board().list_of_points():
            if point.state() == self.color():
                playing_pawns += 1
        return playing_pawns

    def pawns(self):
        # returns sum of playing and unused pawns
        # it decreases while pawns are being taken by opponent
        pawns = self.playing_pawns() + self.unused_pawns()
        return pawns

    def board(self):
        # returns board instance
        return self._board

    def color(self):
        # returns self color
        return self._color

    def opp_color(self):
        # returns the color of the opponent
        # colors of player and his opponent are always white and black
        return self._opp_color

    def has_above_two_pawns(self):
        # checks if player has above to pawns (if less the game is over)
        if (self.pawns() > 2):
            return True
        else:
            return False

    def is_blocked(self):
        # checks if player's pawns are blocked
        # if the player cannot move the game is over
        is_blocked = True
        if self.pawns() == 3:
            return False
            # if player has 3 pawns he can move the pawn at any point he wants
        if self.unused_pawns() != 0:
            is_blocked = False
            # if there are unused pawns you can put them on the board
        elif self.unused_pawns() == 0:
            for point in self.board().list_of_points():
                if point.state() == self.color():
                    for neighbour in point.neighbours():
                        point = self.board().list_of_points()[neighbour]
                        if point.state() == "empty":
                            is_blocked = False
                    # if one of point's neighbours is empty it's not blocked
        return is_blocked

    def available_moves_put(self):
        # returns available putting points
        # if point is empty, you can put your pawn there
        list_of_moves = []
        for point in self.board().list_of_points():
            if point.state() == "empty":
                list_of_moves.append(point.id())
        return list_of_moves

    def available_moves_move_from(self):
        # returns points, from which player can move
        list_of_moves = []
        for point in self.board().list_of_points():
            if_blocked = True
            if self.pawns() == 3:
                if_blocked = False
            for neighbour in point.neighbours():
                if self.board().list_of_points()[neighbour].state() == "empty":
                    if_blocked = False
            if (point.state() == self.color()) and (if_blocked is False):
                # to move the pawn it must have your color and not be blocked
                list_of_moves.append(point.id())
        return list_of_moves

    def available_moves_move_to(self, point1):
        # returns list of points to which you can move from a particular point
        list_of_moves = []
        if self.board().list_of_points()[point1].state() != self.color():
            # starting point must have player's color
            return None
        for point in self.board().list_of_points()[point1].neighbours():
            # checks starting point's neighbours
            if self.board().list_of_points()[point].state() == "empty":
                list_of_moves.append(self.board().list_of_points()[point].id())
        if self.pawns() == 3:
            # if you have 3 pawns, you can move them anywhere
            return self.available_moves_put()
        else:
            return list_of_moves

    def available_moves_take(self):
        # returns list of opponet's points which you can take
        # it deals with situation, when some points are not in trios
        list_of_moves = []
        for point in self.board().list_of_points():
            if (point.state() == self.opp_color()):
                if point.if_trio() is False:
                    # if point is in trio it cannot be taken
                    list_of_moves.append(point.id())
        if list_of_moves == []:
            for point in self.board().list_of_points():
                if (point.state() == self.opp_color()):
                    list_of_moves.append(point.id())
        return list_of_moves

    def available_moves_take_no_trio(self):
        # returns list of opponet's points which you can take
        # it deals with situation, when all points are in trios
        list_of_moves = []
        for point in self.board().list_of_points():
            if (point.state() == self.opp_color()):
                list_of_moves.append(point.id())
        return list_of_moves

    def put_the_pawn(self, point):
        # puts the pawn, one pawn comes from unused pawns to playing pawns
        # a state of the point changes
        self._board.list_of_points()[point].set_state(self.color())
        self._unused_pawns -= 1
        if self._board.list_of_points()[point].if_trio() is True:
            self.take_opposed_pawn()

    def move_the_pawn(self, point1, point2):
        # moves the pawn, states of points change
        # checks if the move exists in available moves
        if self.pawns() == 3:
            self._board.list_of_points()[point1].set_state("empty")
            self._board.list_of_points()[point2].set_state(self.color())
            if self._board.list_of_points()[point2].if_trio() is True:
                self.take_opposed_pawn()
        else:
            if point2 in self.board().list_of_points()[point1].neighbours():
                self._board.list_of_points()[point1].set_state("empty")
                self._board.list_of_points()[point2].set_state(self.color())
                if self._board.list_of_points()[point2].if_trio() is True:
                    self.take_opposed_pawn()


class Human(Player):
    def __init__(self, board, color):
        # Inherits after class player
        # Has attributes: board and color
        super().__init__(board, color)
        self._name = "human"

    def color(self):
        # returns color of the player
        return self._color

    def name(self):
        # returns name of the player
        return self._name

    def move_manager(self):
        # manages a move, decides whether to put or move
        name = self.color() + " " + self.name()
        if (self._unused_pawns > 0):
            # if there are unused pawns, they have to be putted
            print(f"Your options are: {self.available_moves_put()}")

            while True:
                # the loop runs until the user gives valid data
                point = input(f'{name} choose a point to put the pawn: ')
                try:
                    point = int(point)
                    if point in self.available_moves_put():
                        break
                    else:
                        raise WrongPointError
                except WrongPointError:
                    print("Wrong point! Try again!")
                except ValueError:
                    print("Point must be a number!")

            # putting the pawn
            self.put_the_pawn(point)
        else:
            # if there are no unused pawns, player has to move playing pawn
            print(f"Your options are: {self.available_moves_move_from()}")

            while True:
                # the loop runs until the user gives valid data
                # asking a user to input which pawn to move
                point1 = input(f'{name} choose a pawn you want to move: ')
                try:
                    point1 = int(point1)
                    if point1 in self.available_moves_move_from():
                        break
                    else:
                        raise WrongPointError
                except WrongPointError:
                    print("Wrong point! Try again!")
                except ValueError:
                    print("Point must be a number!")

            # checking if number of pawns equals 3
            if(self.pawns() == 3):
                options = self.available_moves_put()
            else:
                options = self.available_moves_move_to(point1)
            print(f"Your options are: {options}")

            while True:
                # the loop runs until the user gives valid data
                # asking a user to input where to move the pawn
                msg = f'{name} choose where do you want to move the pawn: '
                point2 = input(msg)
                try:
                    point2 = int(point2)
                    if point2 in options:
                        break
                    else:
                        raise WrongPointError
                except WrongPointError:
                    print("Wrong point! Try again!")
                except ValueError:
                    print("Point must be a number!")

            # moving the pawn
            self.move_the_pawn(point1, point2)

    def take_opposed_pawn(self):
        # manages and validates taking a pawn
        name = self.color() + " " + self.name()
        if self.available_moves_take() == []:
            # all pawns are in trio
            options = self.available_moves_take_no_trio()
        else:
            # there are some points out of trio to be taken
            options = self.available_moves_take()
        print(f"Your options are {options}")
        while True:
            # the loop runs until the user gives valid data
            # asking a user to input which pawn to take
            msg = f"{name} choose what do you want to take: "
            take = input(msg)
            try:
                take = int(take)
                if take in options:
                    break
                else:
                    raise WrongPointError
            except WrongPointError:
                print("Wrong point! Try again!")
            except ValueError:
                print("Point must be a number!")

        # takes a pawn
        self.board().list_of_points()[take].set_state("empty")


class SmartComputer(Player):
    def __init__(self, board, color):
        # Inherits after class player
        # Has attributes: board and color
        super().__init__(board, color)
        self._name = "smart computer"

    def color(self):
        # returns player's color
        return self._color

    def name(self):
        # returns player's color
        return self._name

    def move_manager(self):
        # manages a move, calls the appropriate function
        if self.color() not in ["white", "black"]:
            raise WrongColorError
        if (self._unused_pawns > 0):
            # if there are unused pawns, computer has to put them
            point = self.where_to_put()
            # where_to_put decides where to put
            point = int(point)
            info = f"Smart computer moves to point {point}"
            print(info)
            # putting the pawn
            self.put_the_pawn(point)
        else:
            # else computer has to move already playing pawn
            point1, point2 = self.where_to_move_get_trio()
            # where_to_move_get_trio is a function on the top of move hierarchy
            # if there is no chance to get a trio it calls next functions
            info = f"Smart computer moves from {point1} to point {point2}"
            print(info)
            # moving the pawn
            self.move_the_pawn(point1, point2)

    def take_opposed_pawn(self):
        if self.available_moves_take() == []:
            # function returns what to take, to disturb the opponent the most
            # if all his pawns are in trios
            take = self.what_to_take()
        else:
            # if he has some points not in trios
            take = self.what_to_take_no_trio()
        # take a pawn
        self.board().list_of_points()[take].set_state("empty")
        print(f"Smart computer took a pawn on point {take}")

    def where_to_put(self):
        # it returns the best point to put the pawn
        # based on hierarchy of values:
        # make_trio, block_trio, enable_max_number_of_trios
        options = self.available_moves_put()

        for option in options:
            # searches for possibilities to make a trio
            point = self.board().list_of_points()[option]
            for trio in point.trios():
                # for every trio
                trio.remove(point.id())
                state1 = self.board().list_of_points()[trio[0]].state()
                state2 = self.board().list_of_points()[trio[1]].state()
                # we take two other points of trio and check their state
                trio.append(point.id())
                trio.sort()
                if(state1 == state2 == self.color()):
                    # we can get make a trio
                    return option

        for option in options:
            # searches for possibilities to block opponent's trio
            point = self.board().list_of_points()[option]
            for trio in point.trios():
                trio.remove(point.id())
                state1 = self.board().list_of_points()[trio[0]].state()
                state2 = self.board().list_of_points()[trio[1]].state()
                trio.append(point.id())
                trio.sort()
                if(state1 == state2 == self.opp_color()):
                    # we can block opponent's trio
                    return option

        max_future_trios = 0
        best_point = options[0]

        for option in options:
            # searches for possibilities to make a possibility
            # for maximal number of trios
            point = self.board().list_of_points()[option]
            future_trios = 0

            for trio in point.trios():
                trio.remove(point.id())
                state1 = self.board().list_of_points()[trio[0]].state()
                state2 = self.board().list_of_points()[trio[1]].state()
                trio.append(point.id())
                trio.sort()
                if(state1 == self.color() and state2 != self.opp_color()):
                    # there is some potential to make a trio in the future
                    # no opponent's pawn in trio and there is one our's
                    future_trios += 1
                elif (state2 == self.color() and state1 != self.opp_color()):
                    future_trios += 1
            # for every point it counts number of future possible trios
            # and then chooses the best option (max_future_trios)
            if future_trios > max_future_trios:
                best_point = option
            max_future_trios = max(max_future_trios, future_trios)
        if max_future_trios == 0:
            # if there is no option to enable future_trios example: first move
            # in other words there is no good move
            # random choice from possible points to be more unpredictable
            return choice(options)
        return best_point

    def where_to_move_get_trio(self):
        # if computer can get a trio it does it
        options = self.available_moves_move_from()

        for option in options:
            moves = self.available_moves_move_to(option)
            for move in moves:
                # for every possible move
                move_point = self.board().list_of_points()[move]
                for trio in move_point.trios():
                    # checks if the pawn comes into trio
                    trio.remove(move_point.id())
                    state1 = self.board().list_of_points()[trio[0]].state()
                    state2 = self.board().list_of_points()[trio[1]].state()
                    trio.append(move_point.id())
                    trio.sort()
                    if(option not in trio):
                        # avoids the situation that a pawn moves in the area
                        # of trio and a new trio is not emerging
                        if(state1 == state2 == self.color()):
                            # returns option to get a trio
                            return option, move
        # if there is no chance to get a trio it tries to block opponent's trio
        point1, point2 = self.where_to_move_block_trio()
        return point1, point2

    def where_to_move_block_trio(self):
        # computer tries to block opponent's trio
        options = self.available_moves_move_from()

        for option in options:
            # for every self pawn
            point = self.board().list_of_points()[option]
            is_blocking = False
            # we check if this pawn is currently blocking some opp_pawns
            # if yes it cannot be pushed in order to not ublock other trio
            for trio in point.trios():
                trio.remove(point.id())
                state1 = self.board().list_of_points()[trio[0]].state()
                state2 = self.board().list_of_points()[trio[1]].state()
                trio.append(point.id())
                trio.sort()
                if(state1 == state2 == self.opp_color()):
                    is_blocking = True

            moves = self.available_moves_move_to(option)
            for move in moves:
                # for every move
                move_point = self.board().list_of_points()[move]
                for trio in move_point.trios():
                    # for every trio of this move_point
                    trio.remove(move_point.id())
                    state1 = self.board().list_of_points()[trio[0]].state()
                    state2 = self.board().list_of_points()[trio[1]].state()
                    trio.append(move_point.id())
                    trio.sort()
                    # it checks if the move blocks something
                    # and does not unblock anything
                    if(state1 == state2 == self.opp_color()):
                        if is_blocking is False:
                            # if yes it returns this option
                            return option, move
        # if there isn't any blocking option we go down in hierarchy
        # and seek for maximize_future_trios function
        point1, point2 = self.where_to_move_maximize_trios()
        return point1, point2

    def where_to_move_maximize_trios(self):
        # maximizes number of future_trios
        # move must add as much future_trios as possible
        # and remove as little as possible
        # it checks a bilance for every move and returns the best
        options = self.available_moves_move_from()
        best_bilance = 0

        for option in options:
            # for every pawn
            moves = self.available_moves_move_to(option)
            option_point = self.board().list_of_points()[option]
            is_blocking = False

            for move in moves:
                # for every move
                move_point = self.board().list_of_points()[move]
                almost_move_trios = 0  # future_trios we will gain
                almost_option_trios = 0  # future_trios we will lose

                option_point.set_state("empty")
                # setting point_state to empty, to function work(look line 778)

                for trio in move_point.trios():
                    # for every trio of the move_point
                    trio.remove(move_point.id())
                    state1 = self.board().list_of_points()[trio[0]].state()
                    state2 = self.board().list_of_points()[trio[1]].state()
                    # we take states of 2 other points of trio
                    trio.append(move_point.id())
                    trio.sort()
                    # we check if in this trio a future_trio is possible
                    if state1 == self.color() and state2 != self.opp_color():
                        almost_move_trios += 1
                    elif state2 == self.color() and state1 != self.opp_color():
                        almost_move_trios += 1
                    # if yes we add one to future_trios_counter

                for trio in option_point.trios():
                    # for every trio of the option_point
                    trio.remove(option_point.id())
                    state1 = self.board().list_of_points()[trio[0]].state()
                    state2 = self.board().list_of_points()[trio[1]].state()
                    # we take states of 2 other points of trio
                    trio.append(option_point.id())
                    trio.sort()
                    if(state1 == state2 == self.opp_color()):
                        # we check if the pawn we want to move isn't blocking
                        # some trio already, if yes we cannot move it
                        is_blocking = True
                    # we check if we lose a chance for future trio by moving so
                    if(state1 == self.color() and state2 != self.opp_color()):
                        almost_option_trios += 1
                    elif state2 == self.color() and state1 != self.opp_color():
                        almost_option_trios += 1
                    # if yes we add one for losed future_trios

                option_point.set_state(f"{self.color()}")
                # resetting point_state

                bilance = almost_move_trios - almost_option_trios
                # we check bilance of lost and gained future_trios
                if is_blocking is True:
                    # if the point is blocking sth we cannot move it
                    bilance = 0
                if bilance > best_bilance:
                    point1, point2 = option, move
                # updating the best bilance
                best_bilance = max(best_bilance, bilance)

        if best_bilance == 0:
            # if best_bilance equals 0 we random.choice our move
            # in order to be unpredictable
            point1 = choice(self.available_moves_move_from())
            point2 = choice(self.available_moves_move_to(point1))
        # returns best move
        return point1, point2

    def what_to_take_no_trio(self):
        # decides which opp_pawn is best to take
        # it must have the biggest number of neighbours of the same color
        # such pawn is most influential and able to make a lot of future_trios
        max_neighbours = -1
        for point in self.board().list_of_points():
            if point.state() == self.opp_color():
                if point.same_color_neighbours() > max_neighbours:
                    if point.if_trio() is False:
                        max_neighbours = point.same_color_neighbours()
                        what_to_take = point.id()
        return what_to_take

    def what_to_take(self):
        # the same function but in case of all pawns being in trios
        max_neighbours = -1
        for point in self.board().list_of_points():
            if point.state() == self.opp_color():
                if point.same_color_neighbours() > max_neighbours:
                    max_neighbours = point.same_color_neighbours()
                    what_to_take = point.id()
        return what_to_take


class StupidComputer(Player):
    def __init__(self, board, color):
        # Inherits after class player
        # Has attributes: board and color
        super().__init__(board, color)
        self._name = "stupid computer"

    def color(self):
        # returns player's color
        return self._color

    def name(self):
        # returns player's name
        return self._name

    def move_manager(self):
        # manages a move just like smart computer
        # if unused pawns exist -> put them on the board
        # else move playing pawn
        # choices from available moves which are methods of Player
        # prints out where did it move
        if (self._unused_pawns > 0):
            point = choice(self.available_moves_put())
            point = int(point)
            info = f"Stupid computer moves to point {point}"
            print(info)
            self.put_the_pawn(point)
        else:
            point1 = choice(self.available_moves_move_from())
            if (self.pawns() != 3):
                # a case when pawns = 3 and not
                point2 = choice(self.available_moves_move_to(point1))
            else:
                point2 = choice(self.available_moves_put())
            info = f"Stupid computer moves from {point1} to point {point2}"
            print(info)
            self.move_the_pawn(point1, point2)

    def take_opposed_pawn(self):
        # is executed when moving pawn gets into trio
        # choices randomly from possible options which pawn to take
        if self.available_moves_take() == []:
            take = choice(self.available_moves_take_no_trio())
        else:
            take = choice(self.available_moves_take())
        # removes pawn
        self.board().list_of_points()[take].set_state("empty")
        # prints out what did it take
        print(f"Stupid computer took a pawn on point {take}")
